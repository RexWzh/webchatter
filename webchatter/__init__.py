"""Top-level package for WebChatter."""

__author__ = """Rex Wang"""
__email__ = '1073853456@qq.com'
__version__ = '0.1.0'

import os, dotenv, requests
from typing import Union
from . import request

def load_envs(env:Union[None, str, dict]=None):
    """Read the environment variables for the API call"""
    global access_token, base_url
    # update the environment variables
    if isinstance(env, str):
        # load the environment file
        dotenv.load_dotenv(env, override=True)
    elif isinstance(env, dict):
        for key, value in env.items():
            os.environ[key] = value
    # initialize the variables
    access_token = os.getenv("OPENAI_ACCESS_TOKEN")
    base_url = os.getenv("API_REVERSE_PROXY")    
    base_url = request.normalize_url(base_url)
    return True

def save_envs(env_file:str):
    """Save the environment variables for the API call"""
    global access_token, base_url
    with open(env_file, "w") as f:
        f.write(f"OPENAI_ACCESS_TOKEN={access_token}\n")
        f.write(f"API_REVERSE_PROXY={base_url}\n")
    return True

# load the environment variables
load_envs()

def debug_log( net_url:str="https://www.baidu.com"
             , timeout:int=5
             , message:str="hello world! 你好！"
             , test_response:bool=True):
    """Debug the API call

    Args:
        net_url (str, optional): The url to test the network. Defaults to "https://www.baidu.com".
        timeout (int, optional): The timeout for the network test. Defaults to 5.
        test_usage (bool, optional): Whether to test the usage status. Defaults to True.
        test_response (bool, optional): Whether to test the hello world. Defaults to True.
    
    Returns:
        bool: True if the debug is finished.
    """
    # Network test
    try:
        requests.get(net_url, timeout=timeout)
    except:
        print("Warning: Network is not available.")
        return False

    ## Base url
    print("\nCheck your base url:")
    print(base_url)


    print("\nDebug is finished.")
    return True
