import speedtest

# print("Loading servers...")
# s.get_servers()
# print("Choosing best server...")
# server = s.get_best_server()
# print(f"Server connected to {server['host']} of location {server['India']}")

def InternetSpeedTest():
    s = speedtest.Speedtest()

    print("Performing download test...")
    download_result = s.download()
    print("Performing upload test...")
    upload_result = s.download()
    ping_result = s.results.ping

    return download_result, upload_result, ping_result