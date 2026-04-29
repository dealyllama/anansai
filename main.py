from prompt_toolkit import PromptSession

def main():
    session = PromptSession()

    while True:
        try:
            text = session.prompt('> ')
        except KeyboardInterrupt:
            print('Ctrl C Trapped, Ctrl D to exit')
        except EOFError:
            break
        else:
            print('You Entered: ', text)

    print('Ciao Bella!')
            
if __name__ == '__main__':
    main()
