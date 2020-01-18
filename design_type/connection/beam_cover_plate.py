from design_type.connection.moment_connection import MomentConnection
from utils.common.component import *
from Common import *
from utils.common.load import Load
import yaml
import os
import shutil
import logging

class BeamCoverPlate(MomentConnection):

    def __init__(self):
        super(BeamCoverPlate, self).__init__()


    def input_values(self, existingvalues={}):

        options_list = []

        if KEY_SECSIZE in existingvalues:
            existingvalue_key_secsize = existingvalues[KEY_SECSIZE]
        else:
            existingvalue_key_secsize = ''

        if KEY_MATERIAL in existingvalues:
            existingvalue_key_mtrl = existingvalues[KEY_MATERIAL]
        else:
            existingvalue_key_mtrl = ''

        if KEY_MOMENT in existingvalues:
            existingvalues_key_moment = existingvalues[KEY_MOMENT]
        else:
            existingvalues_key_moment = ''

        if KEY_SHEAR in existingvalues:
            existingvalue_key_versh = existingvalues[KEY_SHEAR]
        else:
            existingvalue_key_versh = ''

        if KEY_AXIAL in existingvalues:
            existingvalue_key_axial = existingvalues[KEY_AXIAL]
        else:
            existingvalue_key_axial = ''

        if KEY_D in existingvalues:
            existingvalue_key_d = existingvalues[KEY_D]
        else:
            existingvalue_key_d = ''

        if KEY_TYP in existingvalues:
            existingvalue_key_typ = existingvalues[KEY_TYP]
        else:
            existingvalue_key_typ = ''

        if KEY_GRD in existingvalues:
            existingvalue_key_grd = existingvalues[KEY_GRD]
        else:
            existingvalue_key_grd = ''

        if KEY_FLANGEPLATE_PREFERENCES in existingvalues:
            existingvalue_key_fplate_pref = existingvalues[KEY_PLATETHK]
        else:
            existingvalue_key_fplate_pref = ''

        if KEY_FLANGEPLATE_THICKNESS in existingvalues:
            existingvalue_key_fplate_thk = existingvalues[KEY_PLATETHK]
        else:
            existingvalue_key_fplate_thk = ''

        if KEY_WEBPLATE_THICKNESS in existingvalues:
            existingvalue_key_wplate_thk = existingvalues[KEY_PLATETHK]
        else:
            existingvalue_key_wplate_thk = ''

        t16 = (KEY_MODULE, KEY_DISP_BEAMCOVERPLATE, TYPE_MODULE, None, None)
        options_list.append(t16)

        t1 = (None, DISP_TITLE_CM, TYPE_TITLE, None, None)
        options_list.append(t1)

        t4 = (KEY_SECSIZE, KEY_DISP_SECSIZE, TYPE_COMBOBOX, existingvalue_key_secsize, connectdb("Beams"))
        options_list.append(t4)

        t15 = (KEY_IMAGE, None, TYPE_IMAGE, None, None)
        options_list.append(t15)

        t5 = (KEY_MATERIAL, KEY_DISP_MATERIAL, TYPE_COMBOBOX, existingvalue_key_mtrl, VALUES_MATERIAL)
        options_list.append(t5)

        t6 = (None, DISP_TITLE_FSL, TYPE_TITLE, None, None)
        options_list.append(t6)

        t17 = (KEY_MOMENT, KEY_DISP_MOMENT, TYPE_TEXTBOX,existingvalues_key_moment,None)
        options_list.append(t17)

        t7 = (KEY_SHEAR, KEY_DISP_SHEAR, TYPE_TEXTBOX, existingvalue_key_versh, None)
        options_list.append(t7)

        t8 = (KEY_AXIAL, KEY_DISP_AXIAL, TYPE_TEXTBOX, existingvalue_key_axial, None)
        options_list.append(t8)

        t9 = (None, DISP_TITLE_BOLT, TYPE_TITLE, None, None)
        options_list.append(t9)

        t10 = (KEY_D, KEY_DISP_D, TYPE_COMBOBOX_CUSTOMIZED, existingvalue_key_d, VALUES_D)
        options_list.append(t10)

        t11 = (KEY_TYP, KEY_DISP_TYP, TYPE_COMBOBOX, existingvalue_key_typ, VALUES_TYP)
        options_list.append(t11)

        t12 = (KEY_GRD, KEY_DISP_GRD, TYPE_COMBOBOX_CUSTOMIZED, existingvalue_key_grd, VALUES_GRD)
        options_list.append(t12)

        t18 = (None, DISP_TITLE_FLANGESPLICEPLATE, TYPE_TITLE, None, None)
        options_list.append(t18)

        t19 = (KEY_FLANGEPLATE_PREFERENCES, KEY_DISP_FLANGESPLATE_PREFERENCES, TYPE_COMBOBOX, existingvalue_key_fplate_pref, VALUES_FLANGEPLATE_PREFERENCES)
        options_list.append(t19)

        t20 = (KEY_FLANGEPLATE_THICKNESS, KEY_DISP_FLANGESPLATE_THICKNESS, TYPE_COMBOBOX_CUSTOMIZED, existingvalue_key_fplate_thk, VALUES_FLANGEPLATE_THICKNESS)
        options_list.append(t20)

        t21 = (None, DISP_TITLE_WEBSPLICEPLATE, TYPE_TITLE, None, None)
        options_list.append(t21)

        t22 = (KEY_WEBPLATE_THICKNESS, KEY_DISP_WEBPLATE_THICKNESS, TYPE_COMBOBOX_CUSTOMIZED, existingvalue_key_wplate_thk, VALUES_WEBPLATE_THICKNESS)
        options_list.append(t22)

        return options_list

    def set_input_values(self, design_dictionary):
        super(BeamCoverPlate, self).set_input_values(self, design_dictionary)

        self.preference = design_dictionary[KEY_FLANGEPLATE_PREFERENCES]

        self.section = Beam(designation=design_dictionary[KEY_SECSIZE], material_grade=design_dictionary[KEY_MATERIAL])

        self.web_bolt = Bolt(grade=design_dictionary[KEY_GRD], diameter=design_dictionary[KEY_D],
                             bolt_type=design_dictionary[KEY_TYP], material_grade=design_dictionary[KEY_MATERIAL],
                             bolt_hole_type=design_dictionary[KEY_DP_BOLT_HOLE_TYPE],
                             edge_type=design_dictionary[KEY_DP_DETAILING_EDGE_TYPE],
                             mu_f=design_dictionary[KEY_DP_BOLT_SLIP_FACTOR],
                             corrosive_influences=design_dictionary[KEY_DP_DETAILING_CORROSIVE_INFLUENCES])

        self.flange_bolt = Bolt(grade=design_dictionary[KEY_GRD], diameter=design_dictionary[KEY_D],
                                bolt_type=design_dictionary[KEY_TYP], material_grade=design_dictionary[KEY_MATERIAL],
                                bolt_hole_type=design_dictionary[KEY_DP_BOLT_HOLE_TYPE],
                                edge_type=design_dictionary[KEY_DP_DETAILING_EDGE_TYPE],
                                mu_f=design_dictionary[KEY_DP_BOLT_SLIP_FACTOR],
                                corrosive_influences=design_dictionary[KEY_DP_DETAILING_CORROSIVE_INFLUENCES])

        self.flange_plate = Plate(thickness=design_dictionary.get(KEY_FLANGEPLATE_THICKNESS, None),
                                  material_grade=design_dictionary[KEY_MATERIAL],
                                  gap=design_dictionary[KEY_DP_DETAILING_GAP])
        self.web_plate = Plate(thickness=design_dictionary.get(KEY_WEBPLATE_THICKNESS, None),
                               material_grade=design_dictionary[KEY_MATERIAL],
                               gap=design_dictionary[KEY_DP_DETAILING_GAP])

    def get_bolt_details(self):
        self.flange_bolt.calculate_bolt_spacing_limits(bolt_diameter_provided=self.flange_bolt.bolt_diameter[0],
                                                       connecting_plates_tk=[self.flange_plate.thickness[0],
                                                                             self.section.flange_thickness],
                                                       bolt_hole_type=self.flange_bolt.bolt_hole_type)


        if self.preference == "Outside":
            self.flange_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.flange_bolt.bolt_diameter[0],
                                                     bolt_grade_provided=self.flange_bolt.bolt_grade[0],
                                                     connecting_plates_tk=[self.flange_plate.thickness[0],
                                                                           self.section.flange_thickness],
                                                     n_planes=1)
        else:
            self.flange_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.flange_bolt.bolt_diameter[0],
                                                     bolt_grade_provided=self.flange_bolt.bolt_grade[0],
                                                     connecting_plates_tk=[self.flange_plate.thickness[0],
                                                                           self.section.flange_thickness],
                                                     n_planes=2)
        min_plate_height = self.section.flange_width
        max_plate_height = self.section.flange_width
        axial_force_f = self.load.axial_force * self.section.flange_width * self.section.flange_thickness / self.section.area
        flange_force = (((self.load.moment * 1000000) / (self.section.depth - self.section.flange_thickness)) + (
                    axial_force_f * 1000)) / 1000

        self.flange_plate.get_web_plate_details(bolt_dia=self.flange_bolt.bolt_diameter[0],
                                                web_plate_h_min=min_plate_height,
                                                web_plate_h_max=max_plate_height,
                                                bolt_capacity=self.flange_bolt.bolt_capacity,
                                                connecting_plates_tk=[self.flange_plate.thickness[0],
                                                                      self.section.flange_thickness],
                                                bolt_hole_type=self.flange_bolt.bolt_hole_type,
                                                bolt_line_limit=10, axial_load=flange_force,
                                                shear_ecc=False)

        block_shear_capactity = 0
        moment_capacity = 0
        self.flange_plate.get_moment_cacacity(self.flange_plate.fy, self.flange_plate.thickness[0],
                                              self.flange_plate.length)

        ###### # capacity Check for flange = min(block, yielding, rupture)

        A_vn_flange = (self.section.flange_width - self.flange_plate.bolts_one_line * self.flange_plate.dia_hole) * \
                      self.section.flange_thickness
        A_v_flange = self.section.flange_thickness * self.flange_plate.height

        self.section.shear_yielding_capacity = self.tension_member_design_due_to_yielding_of_gross_section(
            A_v=A_v_flange,
            fy=self.flange_plate.fy)

        self.section.shear_rupture_capacity = self.tension_member_design_due_to_rupture_of_critical_section(
            A_vn=A_vn_flange,
            fu=self.flange_plate.fu)
        #  Block shear strength for flange
        Avg = 2 * (self.flange_plate.end_dist_provided + (
                self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided) \
              * self.section.flange_thickness
        Avn = 2 * (self.flange_plate.end_dist_provided + (
                self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided - (
                           self.flange_plate.bolt_line - 0.5) * self.flange_plate.dia_hole) * \
              self.section.flange_thickness
        Atg = (self.section.flange_width - (
                self.flange_plate.bolts_one_line - 1) * self.flange_plate.gauge_provided) \
              * self.section.flange_thickness
        Atn = (self.section.flange_width - (
                (self.flange_plate.bolts_one_line - 1) * self.flange_plate.gauge_provided)
               - (self.flange_plate.bolts_one_line - 1) * self.flange_plate.dia_hole) * \
              self.section.flange_thickness

        self.section.block_shear_capacity = self.block_shear_strength_section(A_vg=Avg, A_vn=Avn, A_tg=Atg, A_tn=Atn,
                                                                              f_u=self.flange_plate.fu,
                                                                              f_y=self.flange_plate.fy)
        if self.section.block_shear_capacity < self.load.axial_force:  # increase thickness todo
            design_status = False
        else:
            pass

        axial_force_f = self.load.axial_force * self.section.flange_width * self.section.flange_thickness / self.section.area
        flange_force = (((self.load.moment * 1000000) / (self.section.depth - self.section.flange_thickness)) + (
                axial_force_f * 1000)) / 1000

        self.flange_plate.shear_yielding(self.flange_plate.length, self.flange_plate.thickness[0],
                                         self.flange_plate.fy)


        # capacity Check for flange_outsite_plate =min(block, yielding, rupture)

        ####Capacity of flange cover plate for bolted Outside #
        if self.preference == "Outside":
            A_vn_flange = (self.section.flange_width - self.flange_plate.bolts_one_line * self.flange_plate.dia_hole) * \
                          self.flange_plate.thickness[0]
            A_v_flange = self.flange_plate.thickness[0] * self.flange_plate.height
            self.flange_plate.shear_yielding_capacity = self.tension_member_design_due_to_yielding_of_gross_section(
                A_v=A_v_flange,
                fy=self.flange_plate.fy)

            self.flange_plate.shear_rupture_capacity = self.tension_member_design_due_to_rupture_of_critical_section(
                A_vn=A_vn_flange,
                fu=self.flange_plate.fu)

            #  Block shear strength for outside flange plate
            i = 0
            while i + 1 < len(self.flange_plate.thickness):
                self.flange_plate.thickness_provided = self.flange_plate.thickness[i]
                Avg = 2 * (self.flange_plate.end_dist_provided + (
                        self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided) * \
                      self.flange_plate.thickness[
                          i]
                Avn = 2 * (self.flange_plate.end_dist_provided + (
                        self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided - (
                                   self.flange_plate.bolt_line - 0.5) * self.flange_plate.dia_hole) * \
                      self.flange_plate.thickness[i]
                Atg = ((self.flange_plate.bolts_one_line - 1) * self.flange_plate.gauge_provided) * \
                      self.flange_plate.thickness[i]
                Atn = (((self.flange_plate.bolts_one_line - 1) * self.flange_plate.gauge_provided) - (
                        self.flange_plate.bolts_one_line - 1) * self.flange_plate.dia_hole) * \
                      self.flange_plate.thickness[i]
                self.flange_plate.block_shear_capacity = self.block_shear_strength_plate(A_vg=Avg, A_vn=Avn, A_tg=Atg,
                                                                                         A_tn=Atn,
                                                                                         f_u=self.flange_plate.fu,
                                                                                         f_y=self.flange_plate.fy)

                if self.flange_plate.block_shear_capacity < self.load.axial_force:  # increase thickness todo
                    i += 1
                else:
                    break
            # Tension_capacity_flange_plate = min(yielding_cap_flange_plate, rupture_cap_flange_plate,
            #                                     self.flange_plate.block_shear_capacity )
            # if Tension_capacity_flange_plate < flange_force:
            #     design_status = False
            # else:
            #     pass

        else:
            # capacity Check for flange_outsite_plate =min(block, yielding, rupture)


            #  yielding,rupture  for  inside flange plate
            flange_plate_height_inside = (
                                                 self.section.flange_width - self.section.web_thickness - self.section.root_radius) / 2 - \
                                         self.flange_plate.bolts_one_line * self.flange_plate.dia_hole
            flange_plate_height_outside = self.flange_plate.thickness[0] * self.flange_plate.height
            A_vn_flange = ((self.flange_plate.height - self.section.web_thickness - 2 * self.section.root_radius) / 2 *
                           self.flange_plate.thickness[0]) / 2
            A_v_flange = (flange_plate_height_outside * self.flange_plate.thickness[0]) + \
                         2 * (flange_plate_height_inside * self.flange_plate.thickness[0])

            self.flange_plate.shear_yielding_capacity = self.tension_member_design_due_to_yielding_of_gross_section(
                A_v=A_v_flange,
                fy=self.flange_plate.fy)
            flange_plate_height_inside = (
                                                     self.section.flange_width - self.section.web_thickness - self.section.root_radius) / 2 - \
                                         self.flange_plate.bolts_one_line * self.flange_plate.dia_hole

            self.flange_plate.shear_rupture_capacity = self.tension_member_design_due_to_rupture_of_critical_section(
                A_vn=A_vn_flange,
                fu=self.flange_plate.fu)

            #  Block shear strength for outside + inside flange plate

            # OUTSIDE
            i = 0
            while i + 1 < len(self.flange_plate.thickness):
                self.flange_plate.thickness_provided = self.flange_plate.thickness[i]

                Avg = 2 * (self.flange_plate.end_dist_provided + (
                        self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided) * self.flange_plate.thickness[
                          0]
                Avn = 2 * (self.flange_plate.end_dist_provided + (
                        self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided - (
                                   self.flange_plate.bolt_line - 0.5) * self.flange_plate.dia_hole) * \
                      self.flange_plate.thickness[0]
                Atg = ((self.flange_plate.bolts_one_line - 1) * self.flange_plate.gauge_provided) * \
                      self.flange_plate.thickness[0]
                Atn = (((self.flange_plate.bolts_one_line - 1) * self.flange_plate.gauge_provided) - (
                        self.flange_plate.bolts_one_line - 1) * self.flange_plate.dia_hole) * self.flange_plate.thickness[0]

                flange_plate_block_shear_capactity_outside = self.block_shear_strength_plate(A_vg=Avg, A_vn=Avn, A_tg=Atg,
                                                                                             A_tn=Atn,
                                                                                             f_u=self.flange_plate.fu,
                                                                                             f_y=self.flange_plate.fy)

                #  Block shear strength for inside flange plate under shear
                Avg = 2 * (self.flange_plate.end_dist_provided + (
                        self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided) \
                      * self.flange_plate.thickness[0]
                Avn = 2 * (self.flange_plate.end_dist_provided + (
                        self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided - (
                                   self.flange_plate.bolt_line - 0.5) * self.flange_plate.dia_hole) * \
                      self.flange_plate.thickness[0]
                Atg = (self.section.flange_width - (self.flange_plate.bolt_line - 1) * self.flange_plate.gauge_provided) * \
                      self.flange_plate.thickness[0]
                Atn = (self.section.flange_width - (
                        (self.flange_plate.bolt_line - 1) * self.flange_plate.gauge_provided) - (
                               self.flange_plate.bolt_line - 1) * self.flange_plate.dia_hole) * self.flange_plate.thickness[
                          0]

                flange_plate_block_shear_capacity_inside = self.block_shear_strength_plate(A_vg=Avg, A_vn=Avn, A_tg=Atg,
                                                                                           A_tn=Atn,
                                                                                           f_u=self.flange_plate.fu,
                                                                                           f_y=self.flange_plate.fy)
                self.flange_plate.block_shear_capacity = flange_plate_block_shear_capactity_outside + flange_plate_block_shear_capacity_inside
                if self.flange_plate.block_shear_capacity < self.load.axial_force:
                    i += 1
                else:
                    break
                # if self.flange_plate.block_shear_capacity < self.load.axial_force:  # increase thickness todo
                #     design_status = False
                # else:
                #     pass
                # Tension_capacity_flange_plate = min(yielding_cap_flange_plate, rupture_cap_flange_plate,
                #                                     self.flange_plate.block_shear_capacity)
                # if Tension_capacity_flange_plate < flange_force:
                #     design_status = False
                # else:
                #     pass

        ##########################################################################
        # Design of web splice plate
        self.web_bolt.calculate_bolt_spacing_limits(bolt_diameter_provided=self.web_bolt.bolt_diameter[0],
                                                    connecting_plates_tk=[self.web_plate.thickness[0],
                                                                          self.section.web_thickness],
                                                    bolt_hole_type=self.web_bolt.bolt_hole_type)
        min_web_plate_height = self.section.min_plate_height()
        max_web_plate_height = self.section.max_plate_height()
        axial_force_w = int(((self.section.depth - 2 * (
            self.section.flange_thickness)) * self.section.web_thickness * self.load.axial_force * 10) / self.section.area) / 1000
        self.web_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.web_bolt.bolt_diameter[0],
                                              bolt_grade_provided=self.web_bolt.bolt_grade[0],
                                              connecting_plates_tk=[self.web_plate.thickness[0],
                                                                    self.section.web_thickness],
                                              n_planes=2)

        self.web_plate.get_web_plate_details(bolt_dia=self.web_bolt.bolt_diameter[0],
                                             web_plate_h_min=min_web_plate_height,
                                             web_plate_h_max=max_web_plate_height,
                                             bolt_capacity=self.web_bolt.bolt_capacity,
                                             connecting_plates_tk=[2 * self.web_plate.thickness[0],
                                                                   self.section.web_thickness],
                                             bolt_hole_type=self.web_bolt.bolt_hole_type,
                                             bolt_line_limit=10, shear_load=self.load.shear_force,
                                             axial_load=axial_force_w,
                                             gap=self.web_plate.gap, shear_ecc=True)

        block_shear_capacity = 0
        moment_capacity = 0
        self.web_plate.get_moment_cacacity(self.web_plate.fy, self.web_plate.thickness[0],
                                           self.web_plate.length)

        ################################ CAPACITY CHECK FOR WEB #####################################################################################

        ###### # capacity Check for web in axial = min(block, yielding, rupture)  Todo

        A_vn_web = (self.section.depth - 2 * self.section.flange_thickness - self.web_plate.bolts_one_line * self.web_plate.dia_hole) * self.section.web_thickness
        A_v_web = (self.section.depth - 2 * self.section.flange_thickness) * self.section.web_thickness

        self.section.shear_yielding_capacity = self.tension_member_design_due_to_yielding_of_gross_section(
            A_v=A_v_web,
            fy=self.web_plate.fy)

        self.section.shear_rupture_capacity = self.tension_member_design_due_to_rupture_of_critical_section(
            A_vn=A_vn_web,
            fu=self.web_plate.fu)
        #  Block shear strength for web
        Avg = 2 * (self.web_plate.end_dist_provided + (
                    self.web_plate.bolt_line - 1) * self.web_plate.pitch_provided) * self.section.web_thickness
        Avn = 2 * (self.web_plate.end_dist_provided + (self.web_plate.bolt_line - 1) * self.web_plate.pitch_provided - (
                self.web_plate.bolts_one_line - 0.5) * self.web_plate.dia_hole) * self.section.web_thickness
        Atg = (self.section.depth - self.section.flange_thickness - (
                    (self.web_plate.bolts_one_line - 1) * self.web_plate.gauge_provided)) * self.section.web_thickness
        Atn = ((self.section.depth - self.section.flange_thickness - (
                    (self.web_plate.bolts_one_line - 1) * self.web_plate.gauge_provided)) - (
                       self.web_plate.bolts_one_line - 0.5) * self.web_plate.dia_hole) * self.section.web_thickness

        self.section.block_shear_capacity = self.block_shear_strength_section(A_vg=Avg, A_vn=Avn, A_tg=Atg, A_tn=Atn,
                                                                              f_u=self.web_plate.fu,
                                                                              f_y=self.web_plate.fy)

        if self.section.block_shear_capacity < self.load.axial_force:  # increase thickness todo
            design_status = False
        else:
            pass
            # Tension_capacity_web_plate = min( self.section.shear_yielding_capacity , self.section.shear_rupture_capacity  ,
            #                                     self.section.block_shear_capacity )
            # if Tension_capacity_web_plate  < web_force:
            #     design_status = False
            # else:
            #     pass
        ###### # capacity Check for web plate  in shear = min(block, yielding, rupture)

        A_vn_web = (self.section.depth - self.section.flange_thickness - self.web_bolt.bolts_one_line * self.web_plate.dia_hole) * self.section.web_thickness
        A_v_web = self.web_plate.thickness[0] * self.web_plate.height
        self.web_plate.shear_yielding_capacity = self.tension_member_design_due_to_yielding_of_gross_section(
            A_v=A_v_web, fy=A_vn_web)
        self.web_plate.shear_rupture_capacity = self.tension_member_design_due_to_rupture_of_critical_section(
            A_vn=A_vn_web, fu=self.web_plate.fu)
        i = 0
        while i + 1 < len(self.web_plate.thickness):
            self.web_plate.thickness_provided = self.web_plate.thickness[i]
            Avg = (self.web_plate.edge_dist_provided + (self.web_bolt.bolts_one_line - 1) * self.web_plate.gauge_provided) * \
                  self.web_plate.thickness[0]
            Avn = (self.web_plate.edge_dist_provided + (
                        self.web_bolt.bolts_one_line - 1) * self.web_plate.gauge_provided - (
                           self.web_bolt.bolts_one_line - 0.5) * self.web_plate.dia_hole) * self.web_plate.thickness[0]
            Atg = ((self.web_plate.bolt_line - 1) * self.web_plate.pitch_provided + self.web_plate.end_dist_provided) * \
                  self.web_plate.thickness[0]
            Atn = ((self.web_plate.bolt_line - 1) * self.web_plate.pitch_provided + (
                        self.web_plate.bolt_line - 1) * self.web_plate.dia_hole + self.web_plate.end_dist_provided) * \
                  self.web_plate.thickness[0]
            self.web_plate.block_shear_capacity = self.block_shear_strength_section(A_vg=Avg, A_vn=Avn, A_tg=Atg, A_tn=Atn,
                                                                                    f_u=self.web_plate.fu,
                                                                                    f_y=self.web_plate.fy)

            if self.web_plate.block_shear_capacity < self.load.axial_force:
                i += 1
            else:
                break
            # Tension_capacity_web_plate = min( self.section.shear_yielding_capacity , self.section.shear_rupture_capacity  ,
            #                                     self.section.block_shear_capacity )
        # if Tension_capacity_web_plate  < web_force:
        #     design_status = False
        # else:
        #     pass

        print(self.section)
        print(self.load)
        print(self.flange_bolt)
        print(self.flange_plate)
        print(self.web_bolt)
        print(self.web_plate)
        print(self.flange_plate.block_shear_capacity)
        print(self.load.axial_force)
        print(self.web_plate.thickness_provided)
        print(self.flange_plate.thickness_provided)
        print(self.web_plate.thickness[0])

        ################################ CAPACITY CHECK #####################################################################################

    @staticmethod
    def block_shear_strength_plate(A_vg, A_vn, A_tg, A_tn, f_u, f_y):  # for flange plate
        """Calculate the block shear strength of bolted connections as per cl. 6.4.1

        Args:
            A_vg: Minimum gross area in shear along bolt line parallel to external force [in sq. mm] (float)
            A_vn: Minimum net area in shear along bolt line parallel to external force [in sq. mm] (float)
            A_tg: Minimum gross area in tension from the bolt hole to the toe of the angle,
                           end bolt line, perpendicular to the line of force, respectively [in sq. mm] (float)
            A_tn: Minimum net area in tension from the bolt hole to the toe of the angle,
                           end bolt line, perpendicular to the line of force, respectively [in sq. mm] (float)
            f_u: Ultimate stress of the plate material in MPa (float)
            f_y: Yield stress of the plate material in MPa (float)

        Return:
            block shear strength of bolted connection in N (float)

        Note:
            Reference:
            IS 800:2007, cl. 6.4.1

        """
        gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']
        gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']
        T_db1 = A_vg * f_y / (math.sqrt(3) * gamma_m0) + 0.9 * A_tn * f_u / gamma_m1
        T_db2 = 0.9 * A_vn * f_u / (math.sqrt(3) * gamma_m1) + A_tg * f_y / gamma_m0
        Tdb = min(T_db1, T_db2)
        Tdb = round(Tdb / 1000, 3)
        return Tdb

        # Function for block shear capacity calculation

    @staticmethod
    def block_shear_strength_section(A_vg, A_vn, A_tg, A_tn, f_u, f_y):
        """Calculate the block shear strength of bolted connections as per cl. 6.4.1

        Args:
            A_vg: Minimum gross area in shear along bolt line parallel to external force [in sq. mm] (float)
            A_vn: Minimum net area in shear along bolt line parallel to external force [in sq. mm] (float)
            A_tg: Minimum gross area in tension from the bolt hole to the toe of the angle,
                           end bolt line, perpendicular to the line of force, respectively [in sq. mm] (float)
            A_tn: Minimum net area in tension from the bolt hole to the toe of the angle,
                           end bolt line, perpendicular to the line of force, respectively [in sq. mm] (float)
            f_u: Ultimate stress of the plate material in MPa (float)
            f_y: Yield stress of the plate material in MPa (float)

        Return:
            block shear strength of bolted connection in N (float)

        Note:
            Reference:
            IS 800:2007, cl. 6.4.1

        """
        gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']
        gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']
        T_db1 = A_vg * f_y / (math.sqrt(3) * gamma_m0) + 0.9 * A_tn * f_u / gamma_m1
        T_db2 = 0.9 * A_vn * f_u / (math.sqrt(3) * gamma_m1) + A_tg * f_y / gamma_m0
        Tdb = min(T_db1, T_db2)
        Tdb = round(Tdb / 1000, 3)
        return Tdb
        # cl 6.2 Design Strength Due to Yielding of Gross Section

    @staticmethod
    def tension_member_design_due_to_yielding_of_gross_section(A_v, fy):
        '''
             Args:
                 A_v (float) Area under shear
                 column_fy (float) Yield stress of column material
             Returns:
                 Capacity of column web in shear yielding
             '''
        gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']
        # A_v = height * thickness
        tdg = (A_v * fy) / (gamma_m0 * 1000)
        return tdg

    @staticmethod
    def tension_member_design_due_to_rupture_of_critical_section(A_vn, fu):
        '''
               Args:
                   A_vn (float) Net area under shear
                   column_fu (float) Ultimate stress of column material
               Returns:
                   Capacity of beam web in shear rupture
               '''

        gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']
        # A_vn = (height- bolts_one_line * dia_hole) * thickness
        T_dn = 0.9 * A_vn * fu / (gamma_m1 * 1000)
        return T_dn


