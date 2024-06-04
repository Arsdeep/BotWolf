# BotWolf - A Discord Bot Powered by Google's Gemini

## [Invite](https://discord.com/oauth2/authorize?client_id=1128531571712995349&permissions=125952&scope=bot)

## Introduction

Welcome to BotWolf, a Python-based Discord bot that leverages Google's Gemini for generating intelligent and contextually relevant responses. BotWolf is designed to interact with users in your Discord server, providing engaging and insightful conversations.

## Features

- **Google Gemini Integration**: Uses Google's Gemini to generate high-quality responses.
- **Interactive Commands**: Supports various commands to interact with users.
- **Easy Setup**: Simple to install and configure.
- **Customizable**: Tailor the bot’s responses and behavior to suit your server’s needs.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/BotWolf.git
   cd BotWolf
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**: Create a `.env` file in the root directory and add your Discord bot token and Gemini API key.
   ```env
   GEMINI_API_KEY=your_gemini_api_key
   DISCORD_TOKEN=your_discord_bot_token
   ```

5. **Run the Bot**:
   ```bash
   python botwolf.py
   ```

## Usage

Once BotWolf is running, you can interact with it using commands mentioned below.

### Basic Commands

- `~status`: BotWolf will show its status
- `~<prompt>`: Ask BotWolf any question, and it will respond using Google Gemini.

### Example

```plaintext
User: ~status
BotWolf: I'm online, @You!

User: ~ask What is the capital of France?
BotWolf: The capital of France is Paris.
```

## Contributing

We welcome contributions to improve BotWolf! Here’s how you can help:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## Acknowledgements

- Thanks to [Google Gemini](https://www.google.com/gemini) for providing the AI capabilities.
- Thanks to the [Discord.py](https://discordpy.readthedocs.io/en/stable/) community for their comprehensive library.

## Support

If you encounter any issues or have questions, feel free to open an issue on this github repository or contact me directly at arsdeepdewangan@gmail.com

---

Enjoy using BotWolf in your Discord server! 🚀

---

*To Add the discord bot in ur Server, Use this link - [Invite](https://discord.com/oauth2/authorize?client_id=1128531571712995349&permissions=125952&scope=bot)*
