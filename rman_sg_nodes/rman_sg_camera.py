from .rman_sg_node import RmanSgNode

class RmanSgCamera(RmanSgNode):

    def __init__(self, rman_scene, sg_node, db_name):
        super().__init__(rman_scene, sg_node, db_name)
        self.cam_matrix = None
        self.res_width = -1
        self.res_height = -1
        self.rman_fov = -1
        self.is_perspective = True

    @property
    def cam_matrix(self):
        return self.__cam_matrix

    @cam_matrix.setter
    def cam_matrix(self, mtx):
        self.__cam_matrix = mtx

    @property
    def res_width(self):
        return self.__res_width

    @res_width.setter
    def res_width(self, res_width):
        self.__res_width = res_width

    @property
    def res_height(self):
        return self.__res_height

    @res_height.setter
    def res_height(self, res_height):
        self.__res_height = res_height  

    @property
    def rman_fov(self):
        return self.__rman_fov

    @rman_fov.setter
    def rman_fov(self, rman_fov):
        self.__rman_fov = rman_fov   

    @property
    def is_perspective(self):
        return self.__is_perspective

    @is_perspective.setter
    def is_perspective(self, is_perspective):
        self.__is_perspective = is_perspective                             
