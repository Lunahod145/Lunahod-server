import uvicorn

from lunohod_server import app


def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=False)


if __name__ == "__main__":
    main()
