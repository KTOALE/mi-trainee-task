from asyncio import get_event_loop


def main():
    loop = get_event_loop()
    loop
    loop.run_forever()

if __name__=="__main__":
    main()