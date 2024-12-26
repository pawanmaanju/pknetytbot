import yt_dlp
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

# Set up logging to get detailed error messages
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to download the YouTube playlist
def download_playlist(url, format_type, quality_or_resolution):
    try:
        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',  # Save each file with its title
        }

        if format_type == 'audio':
            # For audio download, specify audio quality
            ydl_opts['format'] = f'bestaudio[ext=m4a]/bestaudio'
            ydl_opts['audioquality'] = quality_or_resolution
            return f"Downloading audio with quality {quality_or_resolution}..."
        elif format_type == 'video':
            # For video download, specify video quality/resolution
            ydl_opts['format'] = f'bestvideo[height<={quality_or_resolution}]+bestaudio/best'
            return f"Downloading video with resolution {quality_or_resolution}..."
        else:
            return "Invalid format specified. Use 'audio' or 'video'."

        # Download the playlist
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return "Download complete."

    except Exception as e:
        return f"Error occurred: {e}"

# Command to start the bot and provide instructions
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the YouTube Downloader Bot!\n'
                              'Use the following commands:\n'
                              '/download [URL] [format] [quality/resolution]\n'
                              'Example: /download https://www.youtube.com/playlist?list=XXXXX audio 320k')

# Command to download playlist
def download(update: Update, context: CallbackContext) -> None:
    try:
        # Get the input parameters from the message
        args = context.args
        if len(args) < 3:
            update.message.reply_text("Please provide all the required parameters.\n"
                                      "Example: /download https://www.youtube.com/playlist?list=XXXXX audio 320k")
            return

        url = args[0]
        format_type = args[1].lower()  # 'audio' or 'video'
        quality_or_resolution = args[2]  # '320k' for audio or '1080p' for video

        # Call the download function
        status = download_playlist(url, format_type, quality_or_resolution)
        update.message.reply_text(status)

    except Exception as e:
        update.message.reply_text(f"An error occurred: {e}")

def main() -> None:
    # Replace 'YOUR_API_TOKEN' with your actual bot API token
    updater = Updater("7168358367:AAH21vD3sNQIMiV_Qg9NfG0VO1OI81-hdec")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add handlers for commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("download", download))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a stop signal (Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()
