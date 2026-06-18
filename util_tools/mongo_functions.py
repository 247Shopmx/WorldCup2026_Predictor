import logging
from pymongo import MongoClient

logger = logging.getLogger(__name__)

def get_mongo_client(uri='mongodb://192.168.0.77:27017/'):
    """
    Get MongoDB client connection
    
    Args:
        uri (str): MongoDB connection URI
        
    Returns:
        MongoClient: MongoDB client instance
    """
    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        # Verify connection
        client.admin.command('ping')
        logger.info("Successfully connected to MongoDB")
        return client
    except Exception as e:
        logger.error(f"Failed to connect to MongoDB: {str(e)}")
        raise
