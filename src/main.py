import sys
from summarizer import summarize

def main():
    # Check if a file was provided as input
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            text = file.read()
    else:
        # Prompt the user to enter the Arabic text
        text = input("Please enter the Arabic text to summarize: ")

    # Call the summarizer function
    summary = summarize(text)

    # Print the resulting summary
    print("Summary:")
    print(summary)

if __name__ == "__main__":
    main()