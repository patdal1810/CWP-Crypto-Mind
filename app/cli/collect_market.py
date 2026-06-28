from app.market.service import MarketCollectorService


def run():
    service = MarketCollectorService()
    results = service.run()

    print("\nCollection completed.")
    print(results)


if __name__ == "__main__":
    run()