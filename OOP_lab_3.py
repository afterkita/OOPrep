class Array3d:
    def __init__(self, width, height, depth, values):
        self.__width = width
        self.__height = height
        self.__depth = depth
        self.__values = values
        self.__length = width * height * depth
        self.__data = [values] * self.__length

    def __transform_index(self, x, y, z):
        return x + self.__width * (y + self.__height * z)

    def __str__(self):
        result = ""
        for z in range(self.__depth):
            result += f"Глубина: {z}\n"
            for y in range(self.__height):
                for x in range(self.__width):
                    result += f"{self.data[self.__transform_index(x, y, z)]} "
                result += "\n"
            result += "\n"
        return result

    def GetValues_1(self, z):
        result = ""
        for y in range(self.__height):
            result += "\n"
            for x in range(self.__width):
                result += f"{self.data[self.__transform_index(x, y, z)]}"
        return result

    def GetValues_2(self, z, y):
        result = ""
        for x in range(self.__width):
            result += f"{self.data[self.__transform_index(x, y, z)]} "
        return result

    def GetValues_3(self, z, y, x):
        result = f"{self.data[self.__transform_index(x, y, z)]} "
        return result

    def SetValues_1(self, z, array):
        for y in range(self.__height):
            for x in range(self.__width):
                self.data[self.__transform_index(x, y, z)] = array[y][x]

    def SetValues_2(self, z, y, array):
        for x in range(self.__width):
            self.data[self.__transform_index(x, y, z)] = array[x]

    def SetValues_3(self, z, y, x, value):
        self.data[self.__transform_index(x, y, z)] = value

    def npfill(self, values):
        self.data = [values] * self.__length


if __name__ == '__main__':
    array = Array3d(4, 4, 4, 10)
    array.npfill(0)

    array.SetValues_3(0, 0, 0, 1)
    array.SetValues_3(1, 1, 1, 8)

    print(array.GetValues_1(0))
    print('\n')
    print(array.GetValues_2(0, 0))
    print('\n')
    print(array.GetValues_3(0, 0, 0))

    print(array)