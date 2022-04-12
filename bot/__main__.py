from aiogram import Dispatcher
from aiogram.utils.executor import Executor

from settings import config


async def on_startup(dp: Dispatcher):
    pass


async def on_shutdown(dp: Dispatcher):
    from loader import fsm_storage
    await fsm_storage.close()


def main():
    from loader import dispatcher

    executor = Executor(dispatcher)

    executor.on_startup(on_startup)
    executor.on_shutdown(on_shutdown)
    if config.debug:
        executor.start_polling()
    else:
        executor.start_webhook()


if __name__ == '__main__':
    main()
