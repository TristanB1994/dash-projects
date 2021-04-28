from application import init_app

server = init_app()

print(server)
#app.run_server(debug=True, host="0.0.0.0")
if __name__ == "__main__":
    server.run(debug=True, host="0.0.0.0", port="8050")
