from app.utils.common.component import Bolt, Weld, Plate, Angle, Beam, Column


class Input(object):
    pass


class ConnectionInput(Input):
    pass


class ShearConnectionInput(ConnectionInput):

    def __init__(self, connectivity, supporting_member_section, supported_member_section, material):
        self.connectivity = connectivity
        if connectivity == "column_flange_beam_web" or "column_web_beam_web":
            self.supporting_member = Column(supporting_member_section, material)
        elif connectivity == "beam_beam":
            self.supporting_member = Beam(supporting_member_section, material)
        self.supported_member = Beam(supported_member_section, material)
        self.bolt = Bolt()
        self.bolt_diameter_list = []
        self.weld = Weld()
        self.weld_size_list = []


class FinPlateConnectionInput(ShearConnectionInput):

    def __init__(self, connectivity, supporting_member_section, supported_member_section, material):
        self.plate = Plate()
        super(FinPlateConnectionInput, self).__init__(connectivity, supporting_member_section, supported_member_section,
                                                      material)


class EndPlateConnectionInput(ShearConnectionInput):

    def __init__(self, connectivity, supporting_member_section, supported_member_section, material):
        self.plate = Plate()
        super(EndPlateConnectionInput, self).__init__(connectivity, supporting_member_section, supported_member_section,
                                                      material)


class CleatAngleConnectionInput(ShearConnectionInput):

    def __init__(self, connectivity, supporting_member_section, supported_member_section, material):
        self.angle = Angle()
        super(CleatAngleConnectionInput, self).__init__(connectivity, supporting_member_section,
                                                        supported_member_section, material)


class SeatedAngleConnectionInput(ShearConnectionInput):

    def __init__(self, connectivity, supporting_member_section, supported_member_section, material):
        self.angle = Angle()
        super(SeatedAngleConnectionInput, self).__init__(connectivity, supporting_member_section,
                                                         supported_member_section, material)
