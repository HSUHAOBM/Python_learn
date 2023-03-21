queue {
    'maxsize': 0,
    'queue': deque([]),
    'mutex': <unlocked _thread.lock object at 0x000002608DCDAD78>,
    'not_empty': <Condition(<unlocked _thread.lock object at 0x000002608DCDAD78>, 0)>,
    'not_full': <Condition(<unlocked _thread.lock object at 0x000002608DCDAD78>, 0)>,
    'all_tasks_done': <Condition(<unlocked _thread.lock object at 0x000002608DCDAD78>, 0)>,
    'unfinished_tasks': 0
    }


queue {
    'maxsize': 0,
    'queue': deque([('4', 1678780135.1270893)]),
    'mutex': <unlocked _thread.lock object at 0x000002608DCDAD78>,
    'not_empty': <Condition(<unlocked _thread.lock object at 0x000002608DCDAD78>, 0)>,
    'not_full': <Condition(<unlocked _thread.lock object at 0x000002608DCDAD78>, 0)>,
    'all_tasks_done': <Condition(<unlocked _thread.lock object at 0x000002608DCDAD78>, 0)>,
    'unfinished_tasks': 1
}




你的程式碼中使用了 Flask 的單進程模式運行。如果你希望提高你的應用程序的並發性能，你可以考慮使用 Flask 的多進程或多線程模式運行。例如，你可以使用 Gunicorn 或 uWSGI 來啟動 Flask 應用程序，並設置工作進程或工作線程的數量，這樣可以同時處理多個用戶的請求。