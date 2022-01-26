import speedtest

dl = speedtest.Speedtest()
up = speedtest.Speedtest()

servers = dl.get_best_server()

print(dl.results.json())