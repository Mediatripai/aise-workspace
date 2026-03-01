# Global variable
emoticon = ":-)"

def main():
    global emoticon
    say("is anyone there?")
    emoticon = ":-("
    say("oh no, it's gone")

def say(phrase):
    print(phrase + " " + emoticon  )
    

main()