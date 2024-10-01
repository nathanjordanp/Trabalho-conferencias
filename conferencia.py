class Conferencia:

    def __init__(self, id, name, description, image, data, local):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__image = image
        self.__data = data
        self.__local = local


    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_description(self):
        return self.__description
    
    def get_image(self):
        return self.__image

    def get_data(self):
        return self.__data

    def get_local(self):
        return self.__local