import json
import sys
try:
    with open("setting.json", "r", encoding= "utf-8") as file:
        setting_data = json.load(file)

    system_message = setting_data["prompt"]["sys"]

    model_url = setting_data["model"]["url"]
    user_api_key = setting_data["model"]["apikey"]
    model_name = setting_data["model"]["name"]

    function_description = setting_data["prompt"]["func"]["desp"]
    func_parameter_description = setting_data["prompt"]["func"]["para"]

    func_call_choice = setting_data["model"]["tool"]
    if func_call_choice != "force" and func_call_choice != "auto" and func_call_choice != "none":
        sys.exit("setting.json format is wrong")

    web_search_cookie = setting_data["search"]["cookie"]
    web_search_max_num =setting_data["search"]["max_num"]

    server_run_port = setting_data["server"]["port"]
    
    print("init program done")

except FileNotFoundError:
    sys.exit("The setting.json file was not found. Please ensure it exists in the current directory.")
except json.JSONDecodeError:
    sys.exit("Failed to decode JSON from setting.json. Please check the file's format.")
except Exception as e:
    sys.exit(f"An unexpected error occurred: {e}")