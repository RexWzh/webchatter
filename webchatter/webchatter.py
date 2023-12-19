"""Main module."""

from typing import Union
import webchatter
from request import (
    get_account_status, get_models, get_beta_features,
    get_chat_list, get_chat_by_id, 
    continue_chat, create_chat, delete_chat,
)


class WebChat():
    """WebChat class."""
    def __init__( self
                , base_url: Union[str, None] = None
                , access_token: Union[str, None] = None
                , chat_id: Union[str, None] = None
                , node_id: Union[str, None] = None):
        """Initialize the class.

        Args:
            base_url (Union[str, None], optional): The base url for the API. Defaults to None.
            access_token (Union[str, None], optional): The access token for the API. Defaults to None.
            chat_id (Union[str, None], optional): The conversation id for the API. Defaults to None.
            node_id (Union[str, None], optional): The parrent message id for the API. Defaults to None.
        """
        self.base_url = base_url or webchatter.base_url
        self._access_token = access_token or webchatter.access_token
        assert self.base_url is not None, "The base url is not set!"
        assert self.access_token is not None, "The access token is not set!"
        self._conversation_id = chat_id
        self._parrent_message_id = node_id
        self._mapping = {}

    @property
    def access_token(self):
        """Get the access token."""
        return self._access_token
    
    @access_token.setter
    def access_token(self, _):
        """Set the access token."""
        raise AttributeError("The access token cannot be changed. Try to create another chat instead.")
    
    @property
    def chat_id(self):
        """Get the conversation id."""
        return self._conversation_id
    
    @chat_id.setter
    def chat_id(self, _):
        """Set the conversation id."""
        raise AttributeError("The conversation id cannot be changed. Try to create another chat instead.")
    
    @property
    def parrent_message_id(self):
        """Get the parrent message id."""
        return self._parrent_message_id

    @parrent_message_id.setter
    def parrent_message_id(self, _):
        """Set the parrent message id."""
        raise AttributeError("The node id cannot be changed. Please use `self.goto` instead.")

    @property
    def mapping(self):
        """Get the mapping."""
        return self._mapping
    
    @property
    def chat_log(self):
        """Get the chat log."""
        # TODO
    
    def account_status(self):
        """Get the account status."""
        url, token = self.base_url, self.access_token
        resp = get_account_status(url, token)
        return resp['account_plan']
    
    def valid_models(self):
        """Get the models."""
        url, token = self.base_url, self.access_token
        resp = get_models(url, token)
        return [model['category'] for model in resp["categories"]]
    
    def beta_features(self):
        """Get the beta features."""
        url, token = self.base_url, self.access_token
        return get_beta_features(url, token)
    
    def chat_list(self):
        """Get the chat list."""
        url, token = self.base_url, self.access_token
        resp = get_chat_list(url, token)
        return [{'conversation_id':item['id'],'title': item['title']} for item in resp['items']]
    
    def newchat_by_id(self, conversation_id:Union[str, None]=None):
        """Get the chat by id."""
        url, token = self.base_url, self.access_token
        conversation_id = conversation_id or self.conversation_id
        resp = get_chat_by_id(url, token, conversation_id)
        # TODO: extract the chat history
        return WebChat(base_url=url, access_token=token, conversation_id=conversation_id)
    
    def askchat(self, message:str, node_id:Union[str, None]=None):
        """Continue the chat."""
        # TODO
    
    def regenerate(self, message:Union[str, None]=None):
        """Regenerate the chat."""
        # TODO
    
    def goback(self):
        """Go back to the parrent node."""
        # TODO
    
    def goto(self, node_id:str):
        """Go to the parrent node."""
        # TODO

    def save(self, filename:str):
        """Save the chat."""
        # TODO
    
    def load(self, filename:str):
        """Load the chat."""
        # TODO
    
    def print_log(self):
        """Print the chat log."""
        # TODO
    
    def __repr__(self):
        """Representation."""
        # TODO
    
    def __str__(self):
        """String."""
        return self.__repr__()
