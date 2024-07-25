# Leer

Leer is a command-line tool that helps you reading output using OpenAI TTS.

## Installation

Follow these steps to install and set up Leer:

1. Make the script executable:
```sh
chmod +x leer.py
```

2. Create a symbolic link to make it accessible from anywhere:
```sh
sudo ln -s $(pwd)/leer.py /usr/local/bin/leer
```

3. Add `/usr/local/bin` to your PATH if it's not already included:
```sh
export PATH=$PATH:/usr/local/bin
```

4. Source your shell configuration to apply the changes:
```sh
source ~/.zshrc
```

5. Set your OpenAI API key:
```sh
export OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

To use Leer, simply run:

```sh
echo "text to read" | leer
```


## Configuration

Make sure to replace `your_openai_api_key_here` with your actual OpenAI API key. You can add this line to your `~/.zshrc` or `~/.bashrc` to set the API key permanently:

```sh
export OPENAI_API_KEY=sk-your_openai_api_key_here
```

## Contributing

welcomed

## Acknowledgments

- [OpenAI](https://www.openai.com/) for providing the API.
