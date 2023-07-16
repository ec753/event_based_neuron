# converted by json_to_py from 87284_1.json

class Morse_et_al_2010:
    def __init__(self, name=None, x=0, y=0, z=0):
        '''Instantiate Morse_et_al_2010.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, self is used instead
        '''
        self._x, self._y, self._z = x, y, z
        self._name = name
        self._setup_morphology()
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Morse_et_al_2010_instance"

    def _set_section_morphology(self, sec, xyzdiams):
        '''sets the shape and position for a section, shifting it by the offset position'''
        from neuron import h
        h.pt3dclear(sec=sec)
        for pt in xyzdiams:
            x, y, z, diam = pt
            h.pt3dadd(x + self._x, y + self._y, z + self._z, diam, sec=sec)
            
    def _setup_morphology(self):
        self._create_sections()
        self._shape_sections()
        self._connect_sections()
    
    def _insert_mechanisms(self):
        from neuron import h
        for sec in h.allsec():
            sec.insert("pas")
        sec_list0 = [self.apic[0], self.apic[100], self.apic[101], self.apic[102], self.apic[103], self.apic[104], self.apic[105], self.apic[106], self.apic[107], self.apic[108], self.apic[109], self.apic[10], self.apic[110], self.apic[111], self.apic[112], self.apic[113], self.apic[114], self.apic[115], self.apic[116], self.apic[117], self.apic[118], self.apic[119], self.apic[11], self.apic[120], self.apic[121], self.apic[122], self.apic[123], self.apic[124], self.apic[125], self.apic[126], self.apic[127], self.apic[128], self.apic[129], self.apic[12], self.apic[130], self.apic[131], self.apic[132], self.apic[133], self.apic[13], self.apic[14], self.apic[15], self.apic[16], self.apic[17], self.apic[18], self.apic[19], self.apic[1], self.apic[20], self.apic[21], self.apic[22], self.apic[23], self.apic[24], self.apic[25], self.apic[26], self.apic[27], self.apic[28], self.apic[29], self.apic[2], self.apic[30], self.apic[31], self.apic[32], self.apic[33], self.apic[34], self.apic[35], self.apic[36], self.apic[37], self.apic[38], self.apic[39], self.apic[3], self.apic[40], self.apic[41], self.apic[42], self.apic[43], self.apic[44], self.apic[45], self.apic[46], self.apic[47], self.apic[48], self.apic[49], self.apic[4], self.apic[50], self.apic[51], self.apic[52], self.apic[53], self.apic[54], self.apic[55], self.apic[56], self.apic[57], self.apic[58], self.apic[59], self.apic[5], self.apic[60], self.apic[61], self.apic[62], self.apic[63], self.apic[64], self.apic[65], self.apic[66], self.apic[67], self.apic[68], self.apic[69], self.apic[6], self.apic[70], self.apic[71], self.apic[72], self.apic[73], self.apic[74], self.apic[75], self.apic[76], self.apic[77], self.apic[78], self.apic[79], self.apic[7], self.apic[80], self.apic[81], self.apic[82], self.apic[83], self.apic[84], self.apic[85], self.apic[86], self.apic[87], self.apic[88], self.apic[89], self.apic[8], self.apic[90], self.apic[91], self.apic[92], self.apic[93], self.apic[94], self.apic[95], self.apic[96], self.apic[97], self.apic[98], self.apic[99], self.apic[9], self.basal[0], self.basal[10], self.basal[11], self.basal[12], self.basal[13], self.basal[14], self.basal[15], self.basal[16], self.basal[17], self.basal[18], self.basal[19], self.basal[1], self.basal[20], self.basal[21], self.basal[22], self.basal[23], self.basal[24], self.basal[25], self.basal[26], self.basal[27], self.basal[28], self.basal[29], self.basal[2], self.basal[30], self.basal[31], self.basal[32], self.basal[33], self.basal[34], self.basal[35], self.basal[36], self.basal[37], self.basal[38], self.basal[39], self.basal[3], self.basal[40], self.basal[41], self.basal[42], self.basal[43], self.basal[44], self.basal[45], self.basal[46], self.basal[47], self.basal[48], self.basal[49], self.basal[4], self.basal[50], self.basal[51], self.basal[52], self.basal[53], self.basal[54], self.basal[55], self.basal[56], self.basal[57], self.basal[5], self.basal[6], self.basal[7], self.basal[8], self.basal[9], self.soma]
        for sec in sec_list0:
            sec.insert("cacum")
        for sec in sec_list0:
            sec.insert("cagk")
        for sec in sec_list0:
            sec.insert("cal")
        for sec in sec_list0:
            sec.insert("can")
        for sec in sec_list0:
            sec.insert("cat")
        sec_list1 = [self.apic[0], self.apic[100], self.apic[101], self.apic[102], self.apic[103], self.apic[104], self.apic[105], self.apic[106], self.apic[107], self.apic[108], self.apic[109], self.apic[10], self.apic[110], self.apic[111], self.apic[112], self.apic[113], self.apic[114], self.apic[115], self.apic[116], self.apic[117], self.apic[118], self.apic[119], self.apic[11], self.apic[120], self.apic[121], self.apic[122], self.apic[123], self.apic[124], self.apic[125], self.apic[126], self.apic[127], self.apic[128], self.apic[129], self.apic[12], self.apic[130], self.apic[131], self.apic[132], self.apic[133], self.apic[13], self.apic[14], self.apic[15], self.apic[16], self.apic[17], self.apic[18], self.apic[19], self.apic[1], self.apic[20], self.apic[21], self.apic[22], self.apic[23], self.apic[24], self.apic[25], self.apic[26], self.apic[27], self.apic[28], self.apic[29], self.apic[2], self.apic[30], self.apic[31], self.apic[32], self.apic[33], self.apic[34], self.apic[35], self.apic[36], self.apic[37], self.apic[38], self.apic[39], self.apic[3], self.apic[40], self.apic[41], self.apic[42], self.apic[43], self.apic[44], self.apic[45], self.apic[46], self.apic[47], self.apic[48], self.apic[49], self.apic[4], self.apic[50], self.apic[51], self.apic[52], self.apic[53], self.apic[54], self.apic[55], self.apic[56], self.apic[57], self.apic[58], self.apic[59], self.apic[5], self.apic[60], self.apic[61], self.apic[62], self.apic[63], self.apic[64], self.apic[65], self.apic[66], self.apic[67], self.apic[68], self.apic[69], self.apic[6], self.apic[70], self.apic[71], self.apic[72], self.apic[73], self.apic[74], self.apic[75], self.apic[76], self.apic[77], self.apic[78], self.apic[79], self.apic[7], self.apic[80], self.apic[81], self.apic[82], self.apic[83], self.apic[84], self.apic[85], self.apic[86], self.apic[87], self.apic[88], self.apic[89], self.apic[8], self.apic[90], self.apic[91], self.apic[92], self.apic[93], self.apic[94], self.apic[95], self.apic[96], self.apic[97], self.apic[98], self.apic[99], self.apic[9], self.soma]
        for sec in sec_list1:
            sec.insert("ds")
        for sec in sec_list0:
            sec.insert("hd")
        sec_list2 = [self.apic[0], self.apic[100], self.apic[101], self.apic[102], self.apic[103], self.apic[104], self.apic[105], self.apic[106], self.apic[107], self.apic[108], self.apic[109], self.apic[10], self.apic[110], self.apic[111], self.apic[112], self.apic[113], self.apic[114], self.apic[115], self.apic[116], self.apic[117], self.apic[118], self.apic[119], self.apic[11], self.apic[120], self.apic[121], self.apic[122], self.apic[123], self.apic[124], self.apic[125], self.apic[126], self.apic[127], self.apic[128], self.apic[129], self.apic[12], self.apic[130], self.apic[131], self.apic[132], self.apic[133], self.apic[13], self.apic[14], self.apic[15], self.apic[16], self.apic[17], self.apic[18], self.apic[19], self.apic[1], self.apic[20], self.apic[21], self.apic[22], self.apic[23], self.apic[24], self.apic[25], self.apic[26], self.apic[27], self.apic[28], self.apic[29], self.apic[2], self.apic[30], self.apic[31], self.apic[32], self.apic[33], self.apic[34], self.apic[35], self.apic[36], self.apic[37], self.apic[38], self.apic[39], self.apic[3], self.apic[40], self.apic[41], self.apic[42], self.apic[43], self.apic[44], self.apic[45], self.apic[46], self.apic[47], self.apic[48], self.apic[49], self.apic[4], self.apic[50], self.apic[51], self.apic[52], self.apic[53], self.apic[54], self.apic[55], self.apic[56], self.apic[57], self.apic[58], self.apic[59], self.apic[5], self.apic[60], self.apic[61], self.apic[62], self.apic[63], self.apic[64], self.apic[65], self.apic[66], self.apic[67], self.apic[68], self.apic[69], self.apic[6], self.apic[70], self.apic[71], self.apic[72], self.apic[73], self.apic[74], self.apic[75], self.apic[76], self.apic[77], self.apic[78], self.apic[79], self.apic[7], self.apic[80], self.apic[81], self.apic[82], self.apic[83], self.apic[84], self.apic[85], self.apic[86], self.apic[87], self.apic[88], self.apic[89], self.apic[8], self.apic[90], self.apic[91], self.apic[92], self.apic[93], self.apic[94], self.apic[95], self.apic[96], self.apic[97], self.apic[98], self.apic[99], self.apic[9], self.basal[0], self.basal[10], self.basal[11], self.basal[12], self.basal[13], self.basal[14], self.basal[15], self.basal[16], self.basal[17], self.basal[18], self.basal[19], self.basal[1], self.basal[20], self.basal[21], self.basal[22], self.basal[23], self.basal[24], self.basal[25], self.basal[26], self.basal[27], self.basal[28], self.basal[29], self.basal[2], self.basal[30], self.basal[31], self.basal[32], self.basal[33], self.basal[34], self.basal[35], self.basal[36], self.basal[37], self.basal[38], self.basal[39], self.basal[3], self.basal[40], self.basal[41], self.basal[42], self.basal[43], self.basal[44], self.basal[45], self.basal[46], self.basal[47], self.basal[48], self.basal[49], self.basal[4], self.basal[50], self.basal[51], self.basal[52], self.basal[53], self.basal[54], self.basal[55], self.basal[56], self.basal[57], self.basal[5], self.basal[6], self.basal[7], self.basal[8], self.basal[9]]
        for sec in sec_list2:
            sec.insert("kad")
        for sec in sec_list0:
            sec.insert("kap")
        for sec in h.allsec():
            sec.insert("kdr")
        for sec in sec_list0:
            sec.insert("na3")
        sec_list3 = [self.axon]
        for sec in sec_list3:
            sec.insert("nax")
    
    def _set_mechanism_parameters(self):
        for sec in [self.apic[0], self.apic[100], self.apic[101], self.apic[102], self.apic[103], self.apic[104], self.apic[105], self.apic[106], self.apic[107], self.apic[108], self.apic[109], self.apic[10], self.apic[110], self.apic[111], self.apic[112], self.apic[113], self.apic[114], self.apic[115], self.apic[116], self.apic[117], self.apic[118], self.apic[119], self.apic[11], self.apic[120], self.apic[121], self.apic[122], self.apic[123], self.apic[124], self.apic[125], self.apic[126], self.apic[127], self.apic[128], self.apic[129], self.apic[12], self.apic[130], self.apic[131], self.apic[132], self.apic[133], self.apic[13], self.apic[14], self.apic[15], self.apic[16], self.apic[17], self.apic[18], self.apic[19], self.apic[1], self.apic[20], self.apic[21], self.apic[22], self.apic[23], self.apic[24], self.apic[25], self.apic[26], self.apic[27], self.apic[28], self.apic[29], self.apic[2], self.apic[30], self.apic[31], self.apic[32], self.apic[33], self.apic[34], self.apic[35], self.apic[36], self.apic[37], self.apic[38], self.apic[39], self.apic[3], self.apic[40], self.apic[41], self.apic[42], self.apic[43], self.apic[44], self.apic[45], self.apic[46], self.apic[47], self.apic[48], self.apic[49], self.apic[4], self.apic[50], self.apic[51], self.apic[52], self.apic[53], self.apic[54], self.apic[55], self.apic[56], self.apic[57], self.apic[58], self.apic[59], self.apic[5], self.apic[60], self.apic[61], self.apic[62], self.apic[63], self.apic[64], self.apic[65], self.apic[66], self.apic[67], self.apic[68], self.apic[69], self.apic[6], self.apic[70], self.apic[71], self.apic[72], self.apic[73], self.apic[74], self.apic[75], self.apic[76], self.apic[77], self.apic[78], self.apic[79], self.apic[7], self.apic[80], self.apic[81], self.apic[82], self.apic[83], self.apic[84], self.apic[85], self.apic[86], self.apic[87], self.apic[88], self.apic[89], self.apic[8], self.apic[90], self.apic[91], self.apic[92], self.apic[93], self.apic[94], self.apic[95], self.apic[96], self.apic[97], self.apic[98], self.apic[99], self.apic[9], self.axon, self.basal[0], self.basal[10], self.basal[11], self.basal[12], self.basal[13], self.basal[14], self.basal[15], self.basal[16], self.basal[17], self.basal[18], self.basal[19], self.basal[1], self.basal[20], self.basal[21], self.basal[22], self.basal[23], self.basal[24], self.basal[25], self.basal[26], self.basal[27], self.basal[28], self.basal[29], self.basal[2], self.basal[30], self.basal[31], self.basal[32], self.basal[33], self.basal[34], self.basal[35], self.basal[36], self.basal[37], self.basal[38], self.basal[39], self.basal[3], self.basal[40], self.basal[41], self.basal[42], self.basal[43], self.basal[44], self.basal[45], self.basal[46], self.basal[47], self.basal[48], self.basal[49], self.basal[4], self.basal[50], self.basal[51], self.basal[52], self.basal[53], self.basal[54], self.basal[55], self.basal[56], self.basal[57], self.basal[5], self.basal[6], self.basal[7], self.basal[8], self.basal[9], self.soma]:
            sec.cm = 1
            sec.ena = 55
            sec.ek = -90
            sec.gkdrbar_kdr = 0.01
        for sec in [self.apic[0], self.apic[100], self.apic[101], self.apic[102], self.apic[103], self.apic[104], self.apic[105], self.apic[106], self.apic[107], self.apic[108], self.apic[109], self.apic[10], self.apic[110], self.apic[111], self.apic[112], self.apic[113], self.apic[114], self.apic[115], self.apic[116], self.apic[117], self.apic[118], self.apic[119], self.apic[11], self.apic[120], self.apic[121], self.apic[122], self.apic[123], self.apic[124], self.apic[125], self.apic[126], self.apic[127], self.apic[128], self.apic[129], self.apic[12], self.apic[130], self.apic[131], self.apic[132], self.apic[133], self.apic[13], self.apic[14], self.apic[15], self.apic[16], self.apic[17], self.apic[18], self.apic[19], self.apic[1], self.apic[20], self.apic[21], self.apic[22], self.apic[23], self.apic[24], self.apic[25], self.apic[26], self.apic[27], self.apic[28], self.apic[29], self.apic[2], self.apic[30], self.apic[31], self.apic[32], self.apic[33], self.apic[34], self.apic[35], self.apic[36], self.apic[37], self.apic[38], self.apic[39], self.apic[3], self.apic[40], self.apic[41], self.apic[42], self.apic[43], self.apic[44], self.apic[45], self.apic[46], self.apic[47], self.apic[48], self.apic[49], self.apic[4], self.apic[50], self.apic[51], self.apic[52], self.apic[53], self.apic[54], self.apic[55], self.apic[56], self.apic[57], self.apic[58], self.apic[59], self.apic[5], self.apic[60], self.apic[61], self.apic[62], self.apic[63], self.apic[64], self.apic[65], self.apic[66], self.apic[67], self.apic[68], self.apic[69], self.apic[6], self.apic[70], self.apic[71], self.apic[72], self.apic[73], self.apic[74], self.apic[75], self.apic[76], self.apic[77], self.apic[78], self.apic[79], self.apic[7], self.apic[80], self.apic[81], self.apic[82], self.apic[83], self.apic[84], self.apic[85], self.apic[86], self.apic[87], self.apic[88], self.apic[89], self.apic[8], self.apic[90], self.apic[91], self.apic[92], self.apic[93], self.apic[94], self.apic[95], self.apic[96], self.apic[97], self.apic[98], self.apic[99], self.apic[9], self.basal[0], self.basal[10], self.basal[11], self.basal[12], self.basal[13], self.basal[14], self.basal[15], self.basal[16], self.basal[17], self.basal[18], self.basal[19], self.basal[1], self.basal[20], self.basal[21], self.basal[22], self.basal[23], self.basal[24], self.basal[25], self.basal[26], self.basal[27], self.basal[28], self.basal[29], self.basal[2], self.basal[30], self.basal[31], self.basal[32], self.basal[33], self.basal[34], self.basal[35], self.basal[36], self.basal[37], self.basal[38], self.basal[39], self.basal[3], self.basal[40], self.basal[41], self.basal[42], self.basal[43], self.basal[44], self.basal[45], self.basal[46], self.basal[47], self.basal[48], self.basal[49], self.basal[4], self.basal[50], self.basal[51], self.basal[52], self.basal[53], self.basal[54], self.basal[55], self.basal[56], self.basal[57], self.basal[5], self.basal[6], self.basal[7], self.basal[8], self.basal[9], self.soma]:
            sec.Ra = 150
            sec.irest_cacum = -3.63059e-07
            sec.tau_cacum = 40
            sec.cai0_cacum = 5e-05
            sec.gbar_cagk = 5e-05
            sec.gcalbar_cal = 0.0001
            sec.gcanbar_can = 0.0001
            sec.gcatbar_cat = 2.5e-05
            sec.sh_na3 = 0
            sec.gbar_na3 = 0.025
            sec.ar_na3 = 1
        for sec in [self.apic[0], self.apic[100], self.apic[101], self.apic[102], self.apic[103], self.apic[104], self.apic[105], self.apic[106], self.apic[107], self.apic[108], self.apic[109], self.apic[10], self.apic[110], self.apic[111], self.apic[112], self.apic[113], self.apic[114], self.apic[115], self.apic[116], self.apic[117], self.apic[118], self.apic[119], self.apic[11], self.apic[120], self.apic[121], self.apic[122], self.apic[123], self.apic[124], self.apic[125], self.apic[126], self.apic[127], self.apic[128], self.apic[129], self.apic[12], self.apic[130], self.apic[131], self.apic[132], self.apic[133], self.apic[13], self.apic[14], self.apic[15], self.apic[16], self.apic[17], self.apic[18], self.apic[19], self.apic[1], self.apic[20], self.apic[21], self.apic[22], self.apic[2], self.apic[3], self.apic[4], self.apic[5], self.apic[65], self.apic[69], self.apic[6], self.apic[73], self.apic[74], self.apic[77], self.apic[78], self.apic[79], self.apic[7], self.apic[81], self.apic[82], self.apic[83], self.apic[84], self.apic[85], self.apic[86], self.apic[88], self.apic[89], self.apic[8], self.apic[90], self.apic[91], self.apic[92], self.apic[93], self.apic[94], self.apic[95], self.apic[96], self.apic[97], self.apic[98], self.apic[99], self.apic[9], self.axon, self.basal[0], self.basal[10], self.basal[11], self.basal[12], self.basal[13], self.basal[14], self.basal[15], self.basal[16], self.basal[17], self.basal[18], self.basal[19], self.basal[1], self.basal[20], self.basal[21], self.basal[22], self.basal[23], self.basal[24], self.basal[25], self.basal[26], self.basal[27], self.basal[28], self.basal[29], self.basal[2], self.basal[30], self.basal[31], self.basal[32], self.basal[33], self.basal[34], self.basal[35], self.basal[36], self.basal[37], self.basal[38], self.basal[39], self.basal[3], self.basal[40], self.basal[41], self.basal[42], self.basal[43], self.basal[44], self.basal[45], self.basal[46], self.basal[47], self.basal[48], self.basal[49], self.basal[4], self.basal[50], self.basal[51], self.basal[52], self.basal[53], self.basal[54], self.basal[55], self.basal[56], self.basal[57], self.basal[5], self.basal[6], self.basal[7], self.basal[8], self.basal[9], self.soma]:
            sec.g_pas = 3.16228e-05
        for sec in [self.apic[23], self.apic[24], self.apic[25], self.apic[26], self.apic[27], self.apic[28], self.apic[29], self.apic[30], self.apic[31], self.apic[32], self.apic[33], self.apic[34], self.apic[35], self.apic[36], self.apic[37], self.apic[38], self.apic[39], self.apic[40], self.apic[41], self.apic[42], self.apic[43], self.apic[44], self.apic[45], self.apic[46], self.apic[47], self.apic[48], self.apic[49], self.apic[50], self.apic[51], self.apic[52], self.apic[53], self.apic[54], self.apic[55], self.apic[56], self.apic[57], self.apic[58], self.apic[59], self.apic[60], self.apic[61], self.apic[62], self.apic[63], self.apic[64], self.apic[66], self.apic[67], self.apic[68], self.apic[70], self.apic[71], self.apic[72], self.apic[75], self.apic[76], self.apic[80], self.apic[87]]:
            sec.g_pas = 0.000316228
        for sec in [self.apic[100], self.apic[101], self.apic[109], self.apic[110], self.apic[111], self.apic[112], self.apic[114], self.apic[115], self.apic[116], self.apic[117], self.apic[118], self.apic[119], self.apic[120], self.apic[121], self.apic[123], self.apic[124], self.apic[125], self.apic[126], self.apic[127], self.apic[128], self.apic[131], self.apic[132], self.apic[33], self.apic[34], self.apic[35], self.apic[36], self.apic[38], self.apic[39], self.apic[42], self.apic[43], self.apic[45], self.apic[46], self.apic[49], self.apic[50], self.apic[51], self.apic[52], self.apic[57], self.apic[58], self.apic[78], self.apic[79], self.apic[82], self.apic[83], self.apic[85], self.apic[86], self.apic[97], self.apic[98], self.basal[10], self.basal[12], self.basal[13], self.basal[14], self.basal[15], self.basal[20], self.basal[21], self.basal[23], self.basal[24], self.basal[25], self.basal[26], self.basal[32], self.basal[33], self.basal[35], self.basal[36], self.basal[37], self.basal[38], self.basal[39], self.basal[40], self.basal[41], self.basal[42], self.basal[43], self.basal[44], self.basal[46], self.basal[47], self.basal[49], self.basal[4], self.basal[50], self.basal[53], self.basal[54], self.basal[5], self.basal[7], self.basal[8], self.basal[9]]:
            sec.depth_cacum = 0.15
        for sec in [self.apic[129], self.apic[66], self.apic[67], self.apic[70], self.apic[71]]:
            sec.depth_cacum = 0.2
        for sec in [self.apic[103], self.apic[94]]:
            sec.depth_cacum = 0.3
        for sec in [self.apic[26], self.apic[27], self.apic[28]]:
            sec.depth_cacum = 0.6
        for sec in [self.apic[12], self.apic[13], self.apic[14], self.apic[15], self.apic[16], self.apic[17], self.apic[18], self.apic[19], self.apic[20], self.apic[21], self.apic[22], self.apic[23], self.apic[24]]:
            sec.depth_cacum = 0.8
        for sec in [self.apic[10], self.apic[8], self.apic[9]]:
            sec.depth_cacum = 0.9
        for sec in [self.apic[2], self.apic[3], self.apic[4], self.apic[5], self.apic[6]]:
            sec.depth_cacum = 1.1
        for sec in [self.apic[19], self.apic[20], self.apic[21], self.apic[22], self.apic[23], self.apic[24], self.apic[25], self.apic[26], self.apic[27], self.apic[28], self.apic[29], self.apic[30], self.apic[31], self.apic[32], self.apic[33], self.apic[34], self.apic[35], self.apic[36], self.apic[37], self.apic[38], self.apic[39], self.apic[40], self.apic[41], self.apic[42], self.apic[43], self.apic[44], self.apic[45], self.apic[46], self.apic[47], self.apic[48], self.apic[49], self.apic[50], self.apic[51], self.apic[52], self.apic[53], self.apic[54], self.apic[55], self.apic[56], self.apic[57], self.apic[58], self.apic[59], self.apic[60], self.apic[61], self.apic[62], self.apic[63], self.apic[64], self.apic[66], self.apic[67], self.apic[70], self.apic[71], self.apic[82], self.apic[83], self.basal[24], self.basal[37], self.basal[38], self.basal[39], self.basal[40]]:
            sec.ggk_cal = -65.4652
        for sec in [self.apic[16], self.apic[17], self.apic[18], self.apic[65], self.apic[69], self.apic[97], self.apic[98], self.basal[25]]:
            sec.ggk_cal = -65.4652
        for sec in [self.apic[15], self.apic[74], self.basal[13], self.basal[7]]:
            sec.ggk_cal = -65.4652
        for sec in [self.apic[14], self.apic[77]]:
            sec.ggk_cal = -65.4652
        for sec in [self.apic[73], self.basal[12]]:
            sec.ggk_cal = -65.4652
        for sec in [self.apic[115], self.apic[9]]:
            sec.ggk_cal = -65.4652
        for sec in [self.apic[6], self.apic[93]]:
            sec.ggk_cal = -65.4652
        for sec in [self.apic[100], self.apic[101], self.apic[102], self.apic[103], self.apic[104], self.apic[105], self.apic[106], self.apic[107], self.apic[109], self.apic[10], self.apic[110], self.apic[111], self.apic[112], self.apic[116], self.apic[117], self.apic[118], self.apic[119], self.apic[11], self.apic[120], self.apic[121], self.apic[124], self.apic[125], self.apic[126], self.apic[127], self.apic[128], self.apic[12], self.apic[131], self.apic[132], self.apic[133], self.apic[13], self.apic[14], self.apic[15], self.apic[16], self.apic[17], self.apic[18], self.apic[19], self.apic[20], self.apic[21], self.apic[22], self.apic[23], self.apic[24], self.apic[25], self.apic[26], self.apic[27], self.apic[28], self.apic[29], self.apic[30], self.apic[31], self.apic[32], self.apic[33], self.apic[34], self.apic[35], self.apic[36], self.apic[37], self.apic[38], self.apic[39], self.apic[40], self.apic[41], self.apic[42], self.apic[43], self.apic[44], self.apic[45], self.apic[46], self.apic[47], self.apic[48], self.apic[49], self.apic[4], self.apic[50], self.apic[51], self.apic[52], self.apic[53], self.apic[54], self.apic[55], self.apic[56], self.apic[57], self.apic[58], self.apic[59], self.apic[5], self.apic[60], self.apic[61], self.apic[62], self.apic[63], self.apic[64], self.apic[65], self.apic[66], self.apic[67], self.apic[68], self.apic[69], self.apic[6], self.apic[70], self.apic[71], self.apic[72], self.apic[73], self.apic[74], self.apic[75], self.apic[76], self.apic[77], self.apic[78], self.apic[79], self.apic[7], self.apic[80], self.apic[81], self.apic[82], self.apic[83], self.apic[84], self.apic[85], self.apic[86], self.apic[87], self.apic[88], self.apic[89], self.apic[8], self.apic[90], self.apic[91], self.apic[92], self.apic[93], self.apic[94], self.apic[95], self.apic[96], self.apic[97], self.apic[98], self.apic[99], self.apic[9], self.basal[10], self.basal[11], self.basal[12], self.basal[13], self.basal[14], self.basal[15], self.basal[18], self.basal[19], self.basal[20], self.basal[21], self.basal[23], self.basal[24], self.basal[25], self.basal[26], self.basal[31], self.basal[32], self.basal[33], self.basal[36], self.basal[37], self.basal[38], self.basal[39], self.basal[40], self.basal[41], self.basal[43], self.basal[44], self.basal[46], self.basal[47], self.basal[49], self.basal[4], self.basal[50], self.basal[52], self.basal[53], self.basal[54], self.basal[56], self.basal[57], self.basal[5], self.basal[6], self.basal[7], self.basal[8], self.basal[9]]:
            sec.vhalfl_hd = -81
        for sec in [self.apic[0], self.apic[108], self.apic[113], self.apic[114], self.apic[115], self.apic[122], self.apic[123], self.apic[129], self.apic[130], self.apic[1], self.apic[2], self.apic[3], self.basal[0], self.basal[16], self.basal[17], self.basal[1], self.basal[22], self.basal[27], self.basal[28], self.basal[29], self.basal[2], self.basal[30], self.basal[34], self.basal[35], self.basal[3], self.basal[42], self.basal[45], self.basal[48], self.basal[51], self.basal[55], self.soma]:
            sec.vhalfl_hd = -73
        for sec in [self.apic[0], self.apic[108], self.apic[113], self.apic[114], self.apic[115], self.apic[122], self.apic[123], self.apic[129], self.apic[130], self.apic[1], self.apic[2], self.apic[3], self.basal[0], self.basal[16], self.basal[17], self.basal[1], self.basal[22], self.basal[27], self.basal[28], self.basal[29], self.basal[2], self.basal[30], self.basal[34], self.basal[35], self.basal[3], self.basal[42], self.basal[45], self.basal[48], self.basal[51], self.basal[55]]:
            sec.gkabar_kad = 0
        for sec in [self.apic[100], self.apic[101], self.apic[102], self.apic[103], self.apic[104], self.apic[105], self.apic[106], self.apic[10], self.apic[110], self.apic[111], self.apic[112], self.apic[116], self.apic[117], self.apic[11], self.apic[120], self.apic[121], self.apic[125], self.apic[126], self.apic[12], self.apic[13], self.apic[14], self.apic[15], self.apic[16], self.apic[17], self.apic[18], self.apic[19], self.apic[20], self.apic[21], self.apic[22], self.apic[23], self.apic[24], self.apic[25], self.apic[26], self.apic[27], self.apic[28], self.apic[29], self.apic[30], self.apic[31], self.apic[32], self.apic[33], self.apic[34], self.apic[35], self.apic[36], self.apic[37], self.apic[38], self.apic[39], self.apic[40], self.apic[41], self.apic[42], self.apic[43], self.apic[44], self.apic[45], self.apic[46], self.apic[47], self.apic[48], self.apic[49], self.apic[4], self.apic[50], self.apic[51], self.apic[52], self.apic[53], self.apic[54], self.apic[55], self.apic[56], self.apic[57], self.apic[58], self.apic[59], self.apic[5], self.apic[60], self.apic[61], self.apic[62], self.apic[63], self.apic[64], self.apic[65], self.apic[66], self.apic[67], self.apic[68], self.apic[69], self.apic[6], self.apic[70], self.apic[71], self.apic[72], self.apic[73], self.apic[74], self.apic[75], self.apic[76], self.apic[77], self.apic[78], self.apic[79], self.apic[7], self.apic[80], self.apic[81], self.apic[82], self.apic[83], self.apic[84], self.apic[85], self.apic[86], self.apic[87], self.apic[88], self.apic[89], self.apic[8], self.apic[90], self.apic[91], self.apic[92], self.apic[93], self.apic[94], self.apic[95], self.apic[96], self.apic[97], self.apic[98], self.apic[99], self.apic[9], self.basal[10], self.basal[12], self.basal[13], self.basal[14], self.basal[15], self.basal[20], self.basal[21], self.basal[24], self.basal[25], self.basal[32], self.basal[33], self.basal[37], self.basal[38], self.basal[39], self.basal[40], self.basal[46], self.basal[47], self.basal[4], self.basal[53], self.basal[54], self.basal[5], self.basal[7], self.basal[8], self.basal[9]]:
            sec.gkabar_kap = 0
        self.axon.Ra = 50
        self.axon.e_pas = -70.525
        self.axon.sh_nax = 0
        self.axon.gbar_nax = 0.125
        self.apic[3].e_pas = -90.8842
        self.apic[3].ggk_cal = -65.4652
        self.apic[3].ghdbar_hd = 0.000171062
        self.apic[3].gkabar_kap = 0.0542124
        self.basal[35].e_pas = -87.3079
        self.basal[35].ggk_cal = -65.4652
        self.basal[35].ghdbar_hd = 0.000153636
        self.basal[35].gkabar_kap = 0.0507271
        self.basal[42].e_pas = -87.131
        self.basal[42].ggk_cal = -65.4652
        self.basal[42].ghdbar_hd = 0.000152774
        self.basal[42].gkabar_kap = 0.0505548
        self.apic[115].e_pas = -86.5125
        self.apic[115].ghdbar_hd = 0.000192296
        self.apic[115].gkabar_kap = 0.0773461
        self.apic[114].e_pas = -86.0605
        self.apic[114].ggk_cal = -65.4652
        self.apic[114].ghdbar_hd = 0.000170081
        self.apic[114].gkabar_kap = 0.064017
        self.apic[113].e_pas = -85.5519
        self.apic[113].depth_cacum = 0.411714
        self.apic[113].ggk_cal = -65.4652
        self.apic[113].ghdbar_hd = 0.000145079
        self.apic[113].gkabar_kap = 0.0490158
        self.apic[2].e_pas = -85.3969
        self.apic[2].ggk_cal = -65.4652
        self.apic[2].ghdbar_hd = 0.000144324
        self.apic[2].gkabar_kap = 0.0488648
        self.basal[55].e_pas = -85.0158
        self.basal[55].depth_cacum = 0.219518
        self.basal[55].ggk_cal = -65.4652
        self.basal[55].ghdbar_hd = 0.000142467
        self.basal[55].gkabar_kap = 0.0484934
        self.basal[17].e_pas = -83.4422
        self.basal[17].depth_cacum = 0.315938
        self.basal[17].ggk_cal = -65.4652
        self.basal[17].ghdbar_hd = 0.000134799
        self.basal[17].gkabar_kap = 0.0469598
        self.basal[34].e_pas = -82.5356
        self.basal[34].depth_cacum = 0.220592
        self.basal[34].ggk_cal = -65.4652
        self.basal[34].ghdbar_hd = 0.000130382
        self.basal[34].gkabar_kap = 0.0460763
        self.apic[1].e_pas = -80.7174
        self.apic[1].depth_cacum = 1.17187
        self.apic[1].ggk_cal = -65.4652
        self.apic[1].ghdbar_hd = 0.000121522
        self.apic[1].gkabar_kap = 0.0443044
        self.apic[122].e_pas = -79.8672
        self.apic[122].depth_cacum = 0.75
        self.apic[122].ggk_cal = -65.4652
        self.apic[122].ghdbar_hd = 0.000117379
        self.apic[122].gkabar_kap = 0.0434759
        self.basal[30].e_pas = -78.2337
        self.basal[30].depth_cacum = 0.529524
        self.basal[30].ggk_cal = -65.4652
        self.basal[30].ghdbar_hd = 0.00010942
        self.basal[30].gkabar_kap = 0.0418839
        self.basal[16].e_pas = -75.1291
        self.basal[16].depth_cacum = 0.742275
        self.basal[16].ggk_cal = -65.4652
        self.basal[16].ghdbar_hd = 9.42918e-05
        self.basal[16].gkabar_kap = 0.0388584
        self.basal[29].e_pas = -74.9887
        self.basal[29].depth_cacum = 0.717384
        self.basal[29].ggk_cal = -65.4652
        self.basal[29].ghdbar_hd = 9.36076e-05
        self.basal[29].gkabar_kap = 0.0387215
        self.basal[1].e_pas = -73.6303
        self.basal[1].depth_cacum = 0.696139
        self.basal[1].ggk_cal = -65.4652
        self.basal[1].ghdbar_hd = 8.69887e-05
        self.basal[1].gkabar_kap = 0.0373977
        self.basal[28].e_pas = -73.2476
        self.basal[28].depth_cacum = 1
        self.basal[28].ggk_cal = -65.4652
        self.basal[28].ghdbar_hd = 8.51235e-05
        self.basal[28].gkabar_kap = 0.0370247
        self.apic[0].e_pas = -72.098
        self.apic[0].depth_cacum = 1.60145
        self.apic[0].ggk_cal = -65.4652
        self.apic[0].ghdbar_hd = 7.95223e-05
        self.apic[0].gkabar_kap = 0.0359045
        self.basal[27].e_pas = -69.4511
        self.basal[27].depth_cacum = 1.37401
        self.basal[27].ggk_cal = -65.4652
        self.basal[27].ghdbar_hd = 6.66243e-05
        self.basal[27].gkabar_kap = 0.0333249
        self.basal[0].e_pas = -68.3172
        self.basal[0].depth_cacum = 1.55689
        self.basal[0].ggk_cal = -65.4652
        self.basal[0].ghdbar_hd = 6.10995e-05
        self.basal[0].gkabar_kap = 0.0322199
        self.soma.e_pas = -66.0394
        self.soma.depth_cacum = 2.48252
        self.soma.ggk_cal = -65.4652
        self.soma.ghdbar_hd = 5e-05
        self.soma.gkabar_kap = 0.03
        self.apic[23].e_pas = -63.244
        self.apic[23].ghdbar_hd = 0.000583945
        self.apic[23].gkabar_kad = 0.136789
        self.apic[24].e_pas = -63.2326
        self.apic[24].ghdbar_hd = 0.000601795
        self.apic[24].gkabar_kad = 0.140359
        self.apic[56].e_pas = -63.2218
        self.apic[56].depth_cacum = 0.335323
        self.apic[56].ghdbar_hd = 0.000618616
        self.apic[56].gkabar_kad = 0.143723
        self.apic[26].e_pas = -63.1825
        self.apic[26].ghdbar_hd = 0.000679788
        self.apic[26].gkabar_kad = 0.155958
        self.apic[27].e_pas = -63.1636
        self.apic[27].ghdbar_hd = 0.000709279
        self.apic[27].gkabar_kad = 0.161856
        self.apic[28].e_pas = -63.1364
        self.apic[28].ghdbar_hd = 0.000751747
        self.apic[28].gkabar_kad = 0.170349
        self.apic[29].e_pas = -63.1212
        self.apic[29].depth_cacum = 0.575
        self.apic[29].ghdbar_hd = 0.00077536
        self.apic[29].gkabar_kad = 0.175072
        self.apic[30].e_pas = -63.1115
        self.apic[30].depth_cacum = 0.55
        self.apic[30].ghdbar_hd = 0.000790539
        self.apic[30].gkabar_kad = 0.178108
        self.apic[31].e_pas = -63.0905
        self.apic[31].depth_cacum = 0.422072
        self.apic[31].ghdbar_hd = 0.000823172
        self.apic[31].gkabar_kad = 0.184634
        self.apic[32].e_pas = -63.0663
        self.apic[32].depth_cacum = 0.192836
        self.apic[32].ghdbar_hd = 0.000861018
        self.apic[32].gkabar_kad = 0.192204
        self.apic[45].e_pas = -62.9669
        self.apic[45].ghdbar_hd = 0.00101592
        self.apic[45].gkabar_kad = 0.223183
        self.apic[4].e_pas = -49.8703
        self.apic[4].ggk_cal = -65.4652
        self.apic[4].ghdbar_hd = 0.000205222
        self.apic[4].gkabar_kad = 0.0610444
        self.basal[12].e_pas = -49.7147
        self.basal[12].ghdbar_hd = 0.000229472
        self.basal[12].gkabar_kad = 0.0658944
        self.apic[5].e_pas = -49.6852
        self.apic[5].ggk_cal = -65.4652
        self.apic[5].ghdbar_hd = 0.00023408
        self.apic[5].gkabar_kad = 0.0668161
        self.apic[102].e_pas = -49.653
        self.apic[102].depth_cacum = 0.407688
        self.apic[102].ggk_cal = -65.4652
        self.apic[102].ghdbar_hd = 0.000239092
        self.apic[102].gkabar_kad = 0.0678185
        self.apic[6].e_pas = -49.586
        self.apic[6].ghdbar_hd = 0.000249533
        self.apic[6].gkabar_kad = 0.0699066
        self.apic[93].e_pas = -49.5469
        self.apic[93].depth_cacum = 0.576403
        self.apic[93].ghdbar_hd = 0.000255631
        self.apic[93].gkabar_kad = 0.0711263
        self.basal[13].e_pas = -49.5449
        self.basal[13].ghdbar_hd = 0.000255943
        self.basal[13].gkabar_kad = 0.0711885
        self.apic[7].e_pas = -49.4749
        self.apic[7].depth_cacum = 1.06413
        self.apic[7].ggk_cal = -65.4652
        self.apic[7].ghdbar_hd = 0.000266845
        self.apic[7].gkabar_kad = 0.0733691
        self.basal[7].e_pas = -49.3841
        self.basal[7].ghdbar_hd = 0.000281008
        self.basal[7].gkabar_kad = 0.0762017
        self.apic[8].e_pas = -49.3651
        self.apic[8].ggk_cal = -65.4652
        self.apic[8].ghdbar_hd = 0.000283959
        self.apic[8].gkabar_kad = 0.0767918
        self.basal[38].e_pas = -49.35
        self.basal[38].ghdbar_hd = 0.00028632
        self.basal[38].gkabar_kad = 0.077264
        self.apic[9].e_pas = -49.3025
        self.apic[9].ghdbar_hd = 0.000293726
        self.apic[9].gkabar_kad = 0.0787453
        self.apic[88].e_pas = -49.2651
        self.apic[88].depth_cacum = 0.396653
        self.apic[88].ggk_cal = -65.4652
        self.apic[88].ghdbar_hd = 0.000299556
        self.apic[88].gkabar_kad = 0.0799112
        self.apic[10].e_pas = -49.2534
        self.apic[10].ggk_cal = -65.4652
        self.apic[10].ghdbar_hd = 0.000301371
        self.apic[10].gkabar_kad = 0.0802743
        self.apic[11].e_pas = -49.1741
        self.apic[11].depth_cacum = 0.831774
        self.apic[11].ggk_cal = -65.4652
        self.apic[11].ghdbar_hd = 0.00031373
        self.apic[11].gkabar_kad = 0.082746
        self.apic[12].e_pas = -49.0494
        self.apic[12].ggk_cal = -65.4652
        self.apic[12].ghdbar_hd = 0.00033317
        self.apic[12].gkabar_kad = 0.0866341
        self.apic[13].e_pas = -48.8836
        self.apic[13].ggk_cal = -65.4652
        self.apic[13].ghdbar_hd = 0.000359009
        self.apic[13].gkabar_kad = 0.0918019
        self.apic[73].e_pas = -48.7031
        self.apic[73].depth_cacum = 0.518235
        self.apic[73].ghdbar_hd = 0.00038713
        self.apic[73].gkabar_kad = 0.097426
        self.apic[14].e_pas = -48.6168
        self.apic[14].ghdbar_hd = 0.000400581
        self.apic[14].gkabar_kad = 0.100116
        self.apic[15].e_pas = -48.4232
        self.apic[15].ghdbar_hd = 0.000430757
        self.apic[15].gkabar_kad = 0.106151
        self.apic[16].e_pas = -48.321
        self.apic[16].ghdbar_hd = 0.000446687
        self.apic[16].gkabar_kad = 0.109337
        self.apic[69].e_pas = -48.2919
        self.apic[69].depth_cacum = 0.353319
        self.apic[69].ghdbar_hd = 0.000451227
        self.apic[69].gkabar_kad = 0.110245
        self.apic[17].e_pas = -48.2039
        self.apic[17].ghdbar_hd = 0.00046494
        self.apic[17].gkabar_kad = 0.112988
        self.apic[18].e_pas = -48.1268
        self.apic[18].ghdbar_hd = 0.000476948
        self.apic[18].gkabar_kad = 0.11539
        self.apic[19].e_pas = -48.0181
        self.apic[19].ghdbar_hd = 0.000493895
        self.apic[19].gkabar_kad = 0.118779
        self.apic[20].e_pas = -47.8505
        self.apic[20].ghdbar_hd = 0.000520017
        self.apic[20].gkabar_kad = 0.124003
        self.apic[21].e_pas = -47.7376
        self.apic[21].ghdbar_hd = 0.000537606
        self.apic[21].gkabar_kad = 0.127521
        self.apic[22].e_pas = -47.61
        self.apic[22].ghdbar_hd = 0.000557499
        self.apic[22].gkabar_kad = 0.1315
        self.apic[77].e_pas = -44.6245
        self.apic[77].depth_cacum = 0.275
        self.apic[77].ghdbar_hd = 0.000401537
        self.apic[77].gkabar_kad = 0.10607
        self.apic[103].e_pas = -44.0318
        self.apic[103].ggk_cal = -65.4652
        self.apic[103].ghdbar_hd = 0.000258947
        self.apic[103].gkabar_kad = 0.0797315
        self.apic[94].e_pas = -43.3812
        self.apic[94].ggk_cal = -65.4652
        self.apic[94].ghdbar_hd = 0.000277409
        self.apic[94].gkabar_kad = 0.084193
        self.apic[74].e_pas = -39.8586
        self.apic[74].depth_cacum = 0.4
        self.apic[74].ghdbar_hd = 0.00041837
        self.apic[74].gkabar_kad = 0.11617
        for seg, value in zip(self.apic[129], [-67.7155, -71.0679, -74.4203]):
            seg.e_pas = value
        for seg, value in zip(self.apic[129], [-65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[129], [5.81676e-05, 7.45029e-05, 9.08381e-05]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[129], [0.0316335, 0.0349006, 0.0381676]):
            seg.gkabar_kap = value
        for seg, value in zip(self.apic[133], [-60.124, -60.9955, -61.8669, -62.7383, -63.6098, -49.7732, -49.6316]):
            seg.e_pas = value
        for seg, value in zip(self.apic[133], [0.162999, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[133], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[133], [0.000110038, 0.000132104, 0.000154169, 0.000176234, 0.000198299, 0.000220365, 0.00024243]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[133], [0, 0, 0, 0, 0, 0.0640729, 0.068486]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[133], [0.0420077, 0.0464207, 0.0508338, 0.0552468, 0.0596599, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.apic[130], [-78.632, -83.7031, -88.7741]):
            seg.e_pas = value
        for seg, value in zip(self.apic[130], [0.173277, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[130], [-65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[130], [0.000111361, 0.00013607, 0.00016078]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[130], [0.0422721, 0.0472141, 0.052156]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[51], [-74.6779, -78.3081, -81.9383]):
            seg.e_pas = value
        for seg, value in zip(self.basal[51], [0.624103, 0.3, 0.3]):
            seg.depth_cacum = value
        for seg, value in zip(self.basal[51], [-65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[51], [9.20931e-05, 0.000109782, 0.000127471]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[51], [0.0384186, 0.0419564, 0.0454943]):
            seg.gkabar_kap = value
        for seg, value in zip(self.apic[132], [-63.129, -49.8261, -49.6594, -49.4927, -49.326]):
            seg.e_pas = value
        for seg, value in zip(self.apic[132], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[132], [0.000186127, 0.000212111, 0.000238095, 0.000264079, 0.000290063]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[132], [0, 0.0624222, 0.067619, 0.0728158, 0.0780126]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[132], [0.0572254, 0, 0, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.apic[131], [-63.0744, -49.8528, -49.7038, -49.5549, -49.4059, -49.257, -49.108]):
            seg.e_pas = value
        for seg, value in zip(self.apic[131], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[131], [0.000184742, 0.000207957, 0.000231172, 0.000254386, 0.000277601, 0.000300815, 0.00032403]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[131], [0, 0.0615914, 0.0662343, 0.0708772, 0.0755202, 0.0801631, 0.084806]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[131], [0.0569484, 0, 0, 0, 0, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.apic[128], [-57.4347, -53.8996, -50.3646, -23.9804, -17.0965, -10.2126, -3.32862, 3.55532, 10.4393]):
            seg.e_pas = value
        for seg, value in zip(self.apic[128], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[128], [0.000137872, 0.000162187, 0.000186501, 0.000210816, 0.000235131, 0.000259446, 0.000283761, 0.000308076, 0.000332391]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[128], [0, 0, 0, 0.0995381, 0.114127, 0.128716, 0.143305, 0.157894, 0.172483]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[128], [0.0557712, 0.0703602, 0.0849491, 0, 0, 0, 0, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.apic[123], [-80.2245, -80.6, -80.9755]):
            seg.e_pas = value
        for seg, value in zip(self.apic[123], [-65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[123], [0.000134942, 0.000153396, 0.000171851]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[123], [0.0540132, 0.065086, 0.0761588]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[52], [-61.7059, -62.794, -49.8705, -49.6937, -49.517]):
            seg.e_pas = value
        for seg, value in zip(self.basal[52], [0.246874, 0.194348, 0.151588, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.basal[52], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[52], [0.000150091, 0.000177643, 0.000205194, 0.000232745, 0.000260296]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[52], [0, 0, 0.0610388, 0.066549, 0.0720592]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[52], [0.0500183, 0.0555285, 0, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[48], [-75.7816, -80.08, -84.3785]):
            seg.e_pas = value
        for seg, value in zip(self.basal[48], [0.545677, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.basal[48], [-65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[48], [9.74711e-05, 0.000118416, 0.000139361]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[48], [0.0394942, 0.0436832, 0.0478723]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[22], [-81.4576, -85.0466, -88.6356]):
            seg.e_pas = value
        for seg, value in zip(self.basal[22], [0.266095, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.basal[22], [-65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[22], [0.000125129, 0.000142617, 0.000160105]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[22], [0.0450258, 0.0485234, 0.052021]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[11], [-60.2467, -61.1445, -62.0423, -62.9401, -49.8777]):
            seg.e_pas = value
        for seg, value in zip(self.basal[11], [0.233467, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.basal[11], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[11], [0.000113145, 0.000135878, 0.000158611, 0.000181344, 0.000204076]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[11], [0, 0, 0, 0, 0.0608153]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[11], [0.042629, 0.0471756, 0.0517221, 0.0562687, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[2], [-78.3372, -81.6805, -85.0238]):
            seg.e_pas = value
        for seg, value in zip(self.basal[2], [0.410876, 0.301327, 0.3]):
            seg.depth_cacum = value
        for seg, value in zip(self.basal[2], [-65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[2], [0.000109924, 0.000126215, 0.000142506]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[2], [0.0419848, 0.045243, 0.0485012]):
            seg.gkabar_kap = value
        for seg, value in zip(self.apic[127], [-49.4994, -22.739, -16.2985, -9.85795, -3.41743, 3.02309, 9.46361, 15.9041, 22.3447]):
            seg.e_pas = value
        for seg, value in zip(self.apic[127], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[127], [0.000192453, 0.000215201, 0.00023795, 0.000260699, 0.000283447, 0.000306196, 0.000328945, 0.000351694, 0.000374442]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[127], [0, 0.102169, 0.115818, 0.129468, 0.143117, 0.156766, 0.170415, 0.184064, 0.197714]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[127], [0.0885199, 0, 0, 0, 0, 0, 0, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.apic[124], [-49.9776, -25.5325, -20.9543]):
            seg.e_pas = value
        for seg, value in zip(self.apic[124], [-65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[124], [0.000189164, 0.000205334, 0.000221505]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[124], [0, 0.0962489, 0.105951]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[124], [0.0865464, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.apic[119], [-58.5519, -55.8616, -34.0217, -28.7826, -23.5435]):
            seg.e_pas = value
        for seg, value in zip(self.apic[119], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[119], [0.000165411, 0.000183916, 0.000202421, 0.000220927, 0.000239432]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[119], [0, 0, 0.0834212, 0.0945243, 0.105627]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[119], [0.061215, 0.0723181, 0, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.apic[108], [-88.7781, -89.0283, -89.2786]):
            seg.e_pas = value
        for seg, value in zip(self.apic[108], [0.548122, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[108], [-65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[108], [0.000160799, 0.000173101, 0.000185403]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[108], [0.0521599, 0.059541, 0.0669221]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[57], [-62.1289, -63.0914, -49.8426, -49.6862, -49.5298, -49.3735, -49.2171, -49.0607, -48.9043, -48.748, -48.5916, -48.4352, -48.2789]):
            seg.e_pas = value
        for seg, value in zip(self.basal[57], [0.167611, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.basal[57], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[57], [0.000160804, 0.000185175, 0.000209546, 0.000233917, 0.000258288, 0.000282659, 0.00030703, 0.000331401, 0.000355773, 0.000380144, 0.000404515, 0.000428886, 0.000453257]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[57], [0, 0, 0.0619092, 0.0667834, 0.0716576, 0.0765319, 0.0814061, 0.0862803, 0.0911545, 0.0960287, 0.100903, 0.105777, 0.110651]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[57], [0.0521608, 0.057035, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[56], [-62.1113, -63.0387, -49.8569, -49.7062, -49.5556, -49.4049, -49.2542, -49.1036, -48.9529, -48.8023, -48.6516, -48.5009, -48.3503]):
            seg.e_pas = value
        for seg, value in zip(self.basal[56], [0.188423, 0.150031, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.basal[56], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[56], [0.000160358, 0.000183839, 0.000207319, 0.0002308, 0.00025428, 0.000277761, 0.000301241, 0.000324721, 0.000348202, 0.000371682, 0.000395163, 0.000418643, 0.000442124]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[56], [0, 0, 0.0614639, 0.06616, 0.070856, 0.0755521, 0.0802482, 0.0849443, 0.0896404, 0.0943365, 0.0990325, 0.103729, 0.108425]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[56], [0.0520717, 0.0567678, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[54], [-49.3587, -49.219, -49.0793, -48.9395, -48.7998, -48.6601, -48.5204]):
            seg.e_pas = value
        for seg, value in zip(self.basal[54], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[54], [0.00028496, 0.000306736, 0.000328512, 0.000350288, 0.000372064, 0.00039384, 0.000415616]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[54], [0.0769919, 0.0813472, 0.0857024, 0.0900576, 0.0944128, 0.098768, 0.103123]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[53], [-49.3739, -49.2646, -49.1554, -49.0461, -48.9368]):
            seg.e_pas = value
        for seg, value in zip(self.basal[53], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[53], [0.000282588, 0.00029962, 0.000316652, 0.000333684, 0.000350717]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[53], [0.0765176, 0.079924, 0.0833305, 0.0867369, 0.0901433]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[50], [-62.1595, -63.0872, -49.8489, -49.6982, -49.5475, -49.3968, -49.2461, -49.0954, -48.9447, -48.794, -48.6433, -48.4926, -48.3419]):
            seg.e_pas = value
        for seg, value in zip(self.basal[50], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[50], [0.000161578, 0.000185066, 0.000208554, 0.000232042, 0.000255531, 0.000279019, 0.000302507, 0.000325995, 0.000349483, 0.000372971, 0.00039646, 0.000419948, 0.000443436]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[50], [0, 0, 0.0617109, 0.0664085, 0.0711061, 0.0758038, 0.0805014, 0.085199, 0.0898967, 0.0945943, 0.0992919, 0.10399, 0.108687]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[50], [0.0523156, 0.0570132, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[49], [-62.1512, -63.0623, -49.8557, -49.7077, -49.5596, -49.4116, -49.2636, -49.1156, -48.9676, -48.8196, -48.6716, -48.5235, -48.3755]):
            seg.e_pas = value
        for seg, value in zip(self.basal[49], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[49], [0.000161368, 0.000184437, 0.000207505, 0.000230574, 0.000253642, 0.000276711, 0.000299779, 0.000322848, 0.000345916, 0.000368985, 0.000392053, 0.000415122, 0.000438191]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[49], [0, 0, 0.061501, 0.0661148, 0.0707285, 0.0753422, 0.0799559, 0.0845696, 0.0891833, 0.093797, 0.0984107, 0.103024, 0.107638]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[49], [0.0522736, 0.0568873, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[45], [-78.3682, -82.4146, -86.461, -90.5074, -94.5538]):
            seg.e_pas = value
        for seg, value in zip(self.basal[45], [0.287206, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.basal[45], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[45], [0.000110075, 0.000129792, 0.000149509, 0.000169226, 0.000188943]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[45], [0.042015, 0.0459584, 0.0499018, 0.0538452, 0.0577885]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[26], [-62.9568, -49.8551, -49.6894, -49.5236, -49.3579, -49.1921, -49.0264, -48.8607, -48.6949]):
            seg.e_pas = value
        for seg, value in zip(self.basal[26], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[26], [0.000181765, 0.000207596, 0.000233427, 0.000259258, 0.000285089, 0.00031092, 0.000336751, 0.000362582, 0.000388413]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[26], [0, 0.0615191, 0.0666854, 0.0718516, 0.0770178, 0.082184, 0.0873503, 0.0925165, 0.0976827]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[26], [0.0563529, 0, 0, 0, 0, 0, 0, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[23], [-62.8911, -49.8871, -49.7427, -49.5983, -49.4539]):
            seg.e_pas = value
        for seg, value in zip(self.basal[23], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[23], [0.000180102, 0.000202608, 0.000225113, 0.000247619, 0.000270124]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[23], [0, 0.0605215, 0.0650226, 0.0695237, 0.0740249]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[23], [0.0560204, 0, 0, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[19], [-62.2338, -63.0429, -49.8754]):
            seg.e_pas = value
        for seg, value in zip(self.basal[19], [0.236772, 0.152192, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.basal[19], [-65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[19], [0.000163458, 0.000183946, 0.000204434]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[19], [0, 0, 0.0608868]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[19], [0.0526916, 0.0567892, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[18], [-62.3053, -63.2576, -49.8173, -49.6625, -49.5078, -49.3531, -49.1984, -49.0437, -48.889, -48.7343, -48.5796, -48.4248, -48.2701]):
            seg.e_pas = value
        for seg, value in zip(self.basal[18], [0.210519, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.basal[18], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[18], [0.00016527, 0.000189382, 0.000213494, 0.000237607, 0.000261719, 0.000285831, 0.000309943, 0.000334056, 0.000358168, 0.00038228, 0.000406392, 0.000430505, 0.000454617]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[18], [0, 0, 0.0626989, 0.0675213, 0.0723438, 0.0771662, 0.0819887, 0.0868111, 0.0916336, 0.096456, 0.101278, 0.106101, 0.110923]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[18], [0.053054, 0.0578764, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[15], [-49.7499, -49.6402, -49.5306, -49.4209, -49.3112]):
            seg.e_pas = value
        for seg, value in zip(self.basal[15], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[15], [0.000223989, 0.000241081, 0.000258173, 0.000275266, 0.000292358]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[15], [0.0647978, 0.0682162, 0.0716347, 0.0750531, 0.0784716]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[6], [-62.2175, -63.1966, -49.8228, -49.6638, -49.5047]):
            seg.e_pas = value
        for seg, value in zip(self.basal[6], [0.22197, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.basal[6], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[6], [0.000163047, 0.000187836, 0.000212626, 0.000237416, 0.000262206]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[6], [0, 0, 0.0625252, 0.0674832, 0.0724412]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[6], [0.0526093, 0.0575673, 0, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[3], [-88.5274, -92.1911, -95.8549]):
            seg.e_pas = value
        for seg, value in zip(self.basal[3], [0.20945, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.basal[3], [-65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[3], [0.000159578, 0.00017743, 0.000195283]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[3], [0.0519156, 0.0554861, 0.0590565]):
            seg.gkabar_kap = value
        for seg, value in zip(self.apic[126], [-16.2818, -11.515, -6.74822, -1.98142, 2.78538]):
            seg.e_pas = value
        for seg, value in zip(self.apic[126], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[126], [0.000238009, 0.000254846, 0.000271683, 0.00028852, 0.000305357]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[126], [0.115854, 0.125956, 0.136058, 0.14616, 0.156262]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[125], [-15.6366, -9.5792, -3.52185, 2.5355, 8.59286, 14.6502, 20.7076]):
            seg.e_pas = value
        for seg, value in zip(self.apic[125], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[125], [0.000240288, 0.000261683, 0.000283079, 0.000304474, 0.000325869, 0.000347265, 0.00036866]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[125], [0.117221, 0.130058, 0.142895, 0.155733, 0.16857, 0.181407, 0.194244]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[121], [-17.5194, -10.7103, -3.90115, 2.90797, 9.71709]):
            seg.e_pas = value
        for seg, value in zip(self.apic[121], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[121], [0.00026071, 0.00028476, 0.000308811, 0.000332861, 0.000356912]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[121], [0.118394, 0.132824, 0.147255, 0.161685, 0.176116]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[120], [-18.0351, -12.2573, -6.47951, -0.701738, 5.07604, 10.8538, 16.6316]):
            seg.e_pas = value
        for seg, value in zip(self.apic[120], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[120], [0.000258888, 0.000279296, 0.000299704, 0.000320112, 0.000340519, 0.000360927, 0.000381335]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[120], [0.117301, 0.129546, 0.141791, 0.154035, 0.16628, 0.178525, 0.190769]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[118], [-54.1572, -29.353, -22.7643, -16.1756, -9.58682, -2.99808, 3.59066]):
            seg.e_pas = value
        for seg, value in zip(self.apic[118], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[118], [0.000195639, 0.000218912, 0.000242184, 0.000265456, 0.000288728, 0.000312001, 0.000335273]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[118], [0, 0.0933154, 0.107279, 0.121242, 0.135205, 0.149169, 0.163132]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[118], [0.0793521, 0, 0, 0, 0, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.apic[112], [-38.154, -31.5656, -24.9772, -18.3888, -11.8003]):
            seg.e_pas = value
        for seg, value in zip(self.apic[112], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[112], [0.00020319, 0.000226461, 0.000249732, 0.000273003, 0.000296274]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[112], [0.077594, 0.0915567, 0.105519, 0.119482, 0.133445]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[109], [-56.5034, -34.706, -30.2112]):
            seg.e_pas = value
        for seg, value in zip(self.apic[109], [-65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[109], [0.000199492, 0.000215368, 0.000231245]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[109], [0, 0.0849013, 0.094427]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[109], [0.0753755, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.apic[107], [-63.6389, -43.3643, -36.8185, -30.2727, -23.7269, -17.1812, -10.6354, -4.08962, 2.45615, 9.00192, 15.5477]):
            seg.e_pas = value
        for seg, value in zip(self.apic[107], [0.427352, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[107], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[107], [0.000199035, 0.000222156, 0.000245276, 0.000268397, 0.000291517, 0.000314638, 0.000337758, 0.000360879, 0.000383999, 0.00040712, 0.00043024]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[107], [0, 0.0736794, 0.0875516, 0.101424, 0.115296, 0.129168, 0.143041, 0.156913, 0.170785, 0.184658, 0.19853]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[107], [0.0598071, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[47], [-49.8266, -49.6568, -49.487, -49.3172, -49.1474, -48.9776, -48.8078, -48.638, -48.4682]):
            seg.e_pas = value
        for seg, value in zip(self.basal[47], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[47], [0.000212034, 0.000238499, 0.000264964, 0.000291429, 0.000317893, 0.000344358, 0.000370823, 0.000397288, 0.000423753]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[47], [0.0624067, 0.0676997, 0.0729927, 0.0782857, 0.0835787, 0.0888717, 0.0941647, 0.0994577, 0.104751]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[46], [-49.8314, -49.671, -49.5107, -49.3503, -49.19, -49.0296, -48.8693, -48.7089, -48.5486, -48.3883, -48.2279]):
            seg.e_pas = value
        for seg, value in zip(self.basal[46], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[46], [0.000211296, 0.000236286, 0.000261276, 0.000286266, 0.000311256, 0.000336246, 0.000361236, 0.000386226, 0.000411216, 0.000436206, 0.000461196]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[46], [0.0622592, 0.0672572, 0.0722552, 0.0772532, 0.0822512, 0.0872492, 0.0922472, 0.0972451, 0.102243, 0.107241, 0.112239]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[31], [-60.8581, -61.6482, -62.4383, -63.2284, -49.8484]):
            seg.e_pas = value
        for seg, value in zip(self.basal[31], [0.352217, 0.262781, 0.152786, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.basal[31], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[31], [0.000128625, 0.000148631, 0.000168636, 0.000188642, 0.000208647]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[31], [0, 0, 0, 0, 0.0617295]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[31], [0.0457251, 0.0497262, 0.0537273, 0.0577284, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[25], [-49.3223, -49.2034, -49.0846]):
            seg.e_pas = value
        for seg, value in zip(self.basal[25], [0.000290637, 0.000309157, 0.000327677]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[25], [0.0781274, 0.0818315, 0.0855355]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[24], [-49.2991, -49.134, -48.9688, -48.8037, -48.6385, -48.4734, -48.3082]):
            seg.e_pas = value
        for seg, value in zip(self.basal[24], [0.000294247, 0.000319986, 0.000345726, 0.000371465, 0.000397204, 0.000422944, 0.000448683]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[24], [0.0788494, 0.0839972, 0.0891451, 0.094293, 0.0994409, 0.104589, 0.109737]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[21], [-49.7612, -49.6642, -49.5673]):
            seg.e_pas = value
        for seg, value in zip(self.basal[21], [-65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[21], [0.000222233, 0.000237343, 0.000252453]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[21], [0.0644467, 0.0674687, 0.0704907]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[20], [-49.7422, -49.6072, -49.4722, -49.3372, -49.2022, -49.0672, -48.9323]):
            seg.e_pas = value
        for seg, value in zip(self.basal[20], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[20], [0.000225197, 0.000246234, 0.000267272, 0.000288309, 0.000309347, 0.000330384, 0.000351421]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[20], [0.0650394, 0.0692469, 0.0734544, 0.0776619, 0.0818693, 0.0860768, 0.0902843]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[14], [-49.5583, -49.4253, -49.2924, -49.1594, -49.0265, -48.8936, -48.7606]):
            seg.e_pas = value
        for seg, value in zip(self.basal[14], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[14], [0.00025386, 0.000274579, 0.000295297, 0.000316016, 0.000336735, 0.000357453, 0.000378172]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[14], [0.070772, 0.0749158, 0.0790595, 0.0832032, 0.0873469, 0.0914906, 0.0956343]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[10], [-49.3522, -49.2064, -49.0606, -48.9147, -48.7689, -48.623, -48.4772, -48.3313, -48.1855]):
            seg.e_pas = value
        for seg, value in zip(self.basal[10], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[10], [0.000285966, 0.000308697, 0.000331427, 0.000354158, 0.000376888, 0.000399619, 0.00042235, 0.00044508, 0.000467811]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[10], [0.0771932, 0.0817393, 0.0862854, 0.0908316, 0.0953777, 0.0999238, 0.10447, 0.109016, 0.113562]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[5], [-49.8034, -49.6566, -49.5099, -49.3631, -49.2163, -49.0695, -48.9227]):
            seg.e_pas = value
        for seg, value in zip(self.basal[5], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[5], [0.000215648, 0.000238525, 0.000261403, 0.000284281, 0.000307158, 0.000330036, 0.000352913]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[5], [0.0631295, 0.0677051, 0.0722806, 0.0768561, 0.0814316, 0.0860072, 0.0905827]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[4], [-49.7927, -49.6244, -49.4561, -49.2877, -49.1194, -48.9511, -48.7828, -48.6145, -48.4462, -48.2779, -48.1096]):
            seg.e_pas = value
        for seg, value in zip(self.basal[4], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[4], [0.000217325, 0.000243556, 0.000269787, 0.000296019, 0.00032225, 0.000348481, 0.000374713, 0.000400944, 0.000427175, 0.000453407, 0.000479638]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[4], [0.0634649, 0.0687112, 0.0739574, 0.0792037, 0.08445, 0.0896962, 0.0949425, 0.100189, 0.105435, 0.110681, 0.115928]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[117], [-31.1591, -24.3964, -17.6336, -10.8709, -4.10818]):
            seg.e_pas = value
        for seg, value in zip(self.apic[117], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[117], [0.000212532, 0.000236419, 0.000260306, 0.000284193, 0.00030808]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[117], [0.0894879, 0.10382, 0.118152, 0.132484, 0.146816]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[116], [-31.9642, -26.8117, -21.6591, -16.5066, -11.3541]):
            seg.e_pas = value
        for seg, value in zip(self.apic[116], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[116], [0.000209689, 0.000227888, 0.000246088, 0.000264287, 0.000282486]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[116], [0.0877816, 0.0987013, 0.109621, 0.120541, 0.13146]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[111], [-25.5916, -20.8473, -16.1029, -11.3585, -6.61418]):
            seg.e_pas = value
        for seg, value in zip(self.apic[111], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[111], [0.000247561, 0.000264319, 0.000281077, 0.000297834, 0.000314592]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[111], [0.104217, 0.114272, 0.124326, 0.134381, 0.144436]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[110], [-25.495, -20.5573, -15.6196, -10.6819, -5.74428]):
            seg.e_pas = value
        for seg, value in zip(self.apic[110], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[110], [0.000247903, 0.000265343, 0.000282784, 0.000300224, 0.000317665]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[110], [0.104422, 0.114886, 0.125351, 0.135815, 0.146279]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[33], [-49.71, -49.5617, -49.4134, -49.2651, -49.1168, -48.9685, -48.8202]):
            seg.e_pas = value
        for seg, value in zip(self.basal[33], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[33], [0.000230207, 0.00025332, 0.000276434, 0.000299547, 0.00032266, 0.000345774, 0.000368887]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[33], [0.0660413, 0.070664, 0.0752867, 0.0799094, 0.0845321, 0.0891548, 0.0937775]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[32], [-49.7216, -49.5964, -49.4713, -49.3461, -49.221, -49.0958, -48.9707]):
            seg.e_pas = value
        for seg, value in zip(self.basal[32], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[32], [0.000228403, 0.000247909, 0.000267415, 0.000286921, 0.000306427, 0.000325933, 0.000345439]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[32], [0.0656806, 0.0695818, 0.073483, 0.0773842, 0.0812854, 0.0851866, 0.0890878]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[9], [-49.2715, -49.1286, -48.9858, -48.8429, -48.7, -48.5572, -48.4143]):
            seg.e_pas = value
        for seg, value in zip(self.basal[9], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[9], [0.000298549, 0.000320815, 0.000343081, 0.000365347, 0.000387613, 0.000409879, 0.000432145]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[9], [0.0797098, 0.084163, 0.0886162, 0.0930694, 0.0975226, 0.101976, 0.106429]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[8], [-49.2801, -49.1545, -49.0289, -48.9033, -48.7777, -48.6521, -48.5265]):
            seg.e_pas = value
        for seg, value in zip(self.basal[8], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[8], [0.000297203, 0.000316779, 0.000336354, 0.000355929, 0.000375505, 0.00039508, 0.000414655]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[8], [0.0794407, 0.0833557, 0.0872708, 0.0911859, 0.0951009, 0.099016, 0.102931]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[106], [-41.8606, -35.4057, -28.9507, -22.4958, -16.0409, -9.58595, -3.13101, 3.32392, 9.77885, 16.2338, 22.6887]):
            seg.e_pas = value
        for seg, value in zip(self.apic[106], [0.193156, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[106], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[106], [0.000266616, 0.000289416, 0.000312215, 0.000335015, 0.000357815, 0.000380614, 0.000403414, 0.000426213, 0.000449013, 0.000471813, 0.000494612]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[106], [0.0843327, 0.0980125, 0.111692, 0.125372, 0.139052, 0.152732, 0.166411, 0.180091, 0.193771, 0.207451, 0.22113]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[44], [-62.7659, -49.8783, -49.7047, -49.5312, -49.3576, -49.1841, -49.0105]):
            seg.e_pas = value
        for seg, value in zip(self.basal[44], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[44], [0.000176932, 0.000203981, 0.00023103, 0.00025808, 0.000285129, 0.000312178, 0.000339228]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[44], [0, 0.0607962, 0.066206, 0.0716159, 0.0770258, 0.0824357, 0.0878455]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[44], [0.0553863, 0, 0, 0, 0, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[43], [-62.7083, -63.6615, -49.7515, -49.5966, -49.4418, -49.2869, -49.132, -48.9772, -48.8223, -48.6675, -48.5126, -48.3578, -48.2029]):
            seg.e_pas = value
        for seg, value in zip(self.basal[43], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[43], [0.000175474, 0.000199609, 0.000223744, 0.00024788, 0.000272015, 0.00029615, 0.000320285, 0.00034442, 0.000368555, 0.00039269, 0.000416825, 0.00044096, 0.000465095]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[43], [0, 0, 0.0647489, 0.0695759, 0.0744029, 0.0792299, 0.0840569, 0.0888839, 0.0937109, 0.098538, 0.103365, 0.108192, 0.113019]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[43], [0.0550949, 0.0599219, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[41], [-62.8049, -49.8814, -49.7173, -49.5532, -49.389, -49.2249, -49.0608, -48.8967, -48.7326, -48.5685, -48.4043]):
            seg.e_pas = value
        for seg, value in zip(self.basal[41], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[41], [0.00017792, 0.000203498, 0.000229076, 0.000254653, 0.000280231, 0.000305809, 0.000331387, 0.000356965, 0.000382543, 0.000408121, 0.000433699]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[41], [0, 0.0606995, 0.0658151, 0.0709307, 0.0760463, 0.0811618, 0.0862774, 0.091393, 0.0965086, 0.101624, 0.10674]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[41], [0.055584, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.basal[36], [-62.7222, -63.5671, -49.7844, -49.6472, -49.5099]):
            seg.e_pas = value
        for seg, value in zip(self.basal[36], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.basal[36], [0.000175827, 0.000197218, 0.00021861, 0.000240002, 0.000261393]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[36], [0, 0, 0.063722, 0.0680003, 0.0722787]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[36], [0.0551653, 0.0594437, 0, 0, 0]):
            seg.gkabar_kap = value
        for seg, value in zip(self.apic[105], [-39.4745, -32.4726, -25.4708, -18.4689, -11.467]):
            seg.e_pas = value
        for seg, value in zip(self.apic[105], [0.183505, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[105], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[105], [0.000275044, 0.000299776, 0.000324507, 0.000349239, 0.00037397]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[105], [0.0893895, 0.104228, 0.119067, 0.133906, 0.148745]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[104], [-39.2864, -31.9084, -24.5303, -17.1523, -9.77427, -2.39624, 4.9818]):
            seg.e_pas = value
        for seg, value in zip(self.apic[104], [0.184128, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[104], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[104], [0.000275709, 0.000301769, 0.000327829, 0.000353889, 0.000379949, 0.000406009, 0.000432069]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[104], [0.0897881, 0.105424, 0.12106, 0.136696, 0.152332, 0.167968, 0.183605]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[99], [-44.81, -41.2473, -37.6845]):
            seg.e_pas = value
        for seg, value in zip(self.apic[99], [0.25049, 0.163123, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[99], [-65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[99], [0.000272363, 0.000284947, 0.000297531]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[99], [0.081165, 0.0887155, 0.0962659]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[92], [-49.4864, -43.1572, -36.8279, -30.4986, -24.1693, -17.84, -11.5107, -5.18139, 1.1479]):
            seg.e_pas = value
        for seg, value in zip(self.apic[92], [0.528788, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[92], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[92], [0.000265052, 0.000287408, 0.000309763, 0.000332119, 0.000354475, 0.000376831, 0.000399187, 0.000421543, 0.000443898]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[92], [0.0730103, 0.0864238, 0.0998373, 0.113251, 0.126664, 0.140078, 0.153491, 0.166905, 0.180318]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[37], [-49.3604, -49.1985, -49.0366, -48.8748, -48.7129, -48.551, -48.3892]):
            seg.e_pas = value
        for seg, value in zip(self.basal[37], [0.000284703, 0.00030993, 0.000335157, 0.000360384, 0.000385611, 0.000410838, 0.000436065]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[37], [0.0769405, 0.081986, 0.0870314, 0.0920768, 0.0971222, 0.102168, 0.107213]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[101], [-32.9683, -27.0985, -21.2288, -15.3591, -9.48932]):
            seg.e_pas = value
        for seg, value in zip(self.apic[101], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[101], [0.000314189, 0.000334922, 0.000355654, 0.000376387, 0.00039712]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[101], [0.106261, 0.1187, 0.13114, 0.14358, 0.156019]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[100], [-32.5475, -25.8362, -19.1249, -12.4136, -5.70231, 1.00899, 7.72028, 14.4316, 21.1429]):
            seg.e_pas = value
        for seg, value in zip(self.apic[100], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[100], [0.000315675, 0.00033938, 0.000363086, 0.000386791, 0.000410496, 0.000434201, 0.000457906, 0.000481611, 0.000505316]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[100], [0.107153, 0.121376, 0.135599, 0.149822, 0.164045, 0.178268, 0.192491, 0.206714, 0.220937]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[96], [-37.6464, -32.5972, -27.548, -22.4987, -17.4495]):
            seg.e_pas = value
        for seg, value in zip(self.apic[96], [0.208668, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[96], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[96], [0.000297665, 0.0003155, 0.000333334, 0.000351169, 0.000369003]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[96], [0.0963466, 0.107047, 0.117748, 0.128449, 0.139149]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[95], [-36.5047, -29.1721, -21.8395, -14.507, -7.17435, 0.158242, 7.49084]):
            seg.e_pas = value
        for seg, value in zip(self.apic[95], [0.19535, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[95], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[95], [0.000301698, 0.000327598, 0.000353497, 0.000379397, 0.000405296, 0.000431196, 0.000457096]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[95], [0.0987662, 0.114306, 0.129846, 0.145385, 0.160925, 0.176465, 0.192005]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[91], [-49.3052, -41.6701, -34.035, -26.3999, -18.7648, -11.1296, -3.49454, 4.14057, 11.7757]):
            seg.e_pas = value
        for seg, value in zip(self.apic[91], [0.334813, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[91], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[91], [0.000293301, 0.000320269, 0.000347237, 0.000374205, 0.000401174, 0.000428142, 0.00045511, 0.000482078, 0.000509046]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[91], [0.0786602, 0.0948411, 0.111022, 0.127203, 0.143384, 0.159565, 0.175745, 0.191926, 0.208107]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[40], [-49.1763, -49.0115, -48.8467, -48.682, -48.5172, -48.3524, -48.1877]):
            seg.e_pas = value
        for seg, value in zip(self.basal[40], [0.00031339, 0.00033907, 0.000364749, 0.000390429, 0.000416108, 0.000441788, 0.000467467]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[40], [0.0826781, 0.087814, 0.0929499, 0.0980858, 0.103222, 0.108358, 0.113493]):
            seg.gkabar_kad = value
        for seg, value in zip(self.basal[39], [-49.1801, -49.023, -48.8658, -48.7087, -48.5516, -48.3944, -48.2373]):
            seg.e_pas = value
        for seg, value in zip(self.basal[39], [0.000312795, 0.000337285, 0.000361774, 0.000386264, 0.000410753, 0.000435243, 0.000459732]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.basal[39], [0.0825591, 0.087457, 0.0923549, 0.0972528, 0.102151, 0.107049, 0.111946]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[98], [-12.5084, -7.67539, -2.84238, 1.99063, 6.82365]):
            seg.e_pas = value
        for seg, value in zip(self.apic[98], [0.000386456, 0.000403527, 0.000420597, 0.000437668, 0.000454739]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[98], [0.149621, 0.159863, 0.170106, 0.180348, 0.190591]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[97], [-11.5856, -4.90687, 1.77183, 8.45052, 15.1292]):
            seg.e_pas = value
        for seg, value in zip(self.apic[97], [0.000389715, 0.000413305, 0.000436895, 0.000460485, 0.000484075]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[97], [0.151577, 0.165731, 0.179885, 0.194039, 0.208193]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[90], [-43.1342, -37.3589, -31.5835, -25.8082, -20.0328, -14.2575, -8.48213]):
            seg.e_pas = value
        for seg, value in zip(self.apic[90], [0.212863, 0.154455, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[90], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[90], [0.000321211, 0.00034161, 0.000362009, 0.000382409, 0.000402808, 0.000423207, 0.000443606]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[90], [0.0929041, 0.105144, 0.117383, 0.129623, 0.141862, 0.154102, 0.166341]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[89], [-42.1995, -34.5546, -26.9098, -19.2649, -11.62, -3.97517, 3.66969]):
            seg.e_pas = value
        for seg, value in zip(self.apic[89], [0.173362, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[89], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[89], [0.000324512, 0.000351515, 0.000378518, 0.00040552, 0.000432523, 0.000459525, 0.000486528]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[89], [0.0948851, 0.111087, 0.127288, 0.14349, 0.159691, 0.175893, 0.192094]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[87], [-63.4185, -62.7009, -61.9832, -61.2656, -60.5479, -59.8303, -59.1126, -58.395, -57.6773, -56.9597, -56.242, -55.5243, -54.8067]):
            seg.e_pas = value
        for seg, value in zip(self.apic[87], [0.381142, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[87], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[87], [0.000312026, 0.000337374, 0.000362723, 0.000388071, 0.000413419, 0.000438767, 0.000464116, 0.000489464, 0.000514812, 0.000540161, 0.000565509, 0.000590857, 0.000616205]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[87], [0.0824052, 0.0976142, 0.112823, 0.128032, 0.143241, 0.15845, 0.173659, 0.188868, 0.204077, 0.219286, 0.234495, 0.249704, 0.264913]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[84], [-49.196, -45.2762, -41.3565]):
            seg.e_pas = value
        for seg, value in zip(self.apic[84], [0.462728, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[84], [-65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[84], [0.000310313, 0.000324159, 0.000338004]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[84], [0.0820627, 0.0903698, 0.0986769]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[86], [-35.8331, -28.7063, -21.5794, -14.4526, -7.32571, -0.198854, 6.928, 14.0549, 21.1817]):
            seg.e_pas = value
        for seg, value in zip(self.apic[86], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[86], [0.000357513, 0.000382686, 0.000407859, 0.000433032, 0.000458204, 0.000483377, 0.00050855, 0.000533723, 0.000558896]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[86], [0.110382, 0.125486, 0.14059, 0.155694, 0.170797, 0.185901, 0.201005, 0.216109, 0.231212]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[85], [-35.6582, -28.1816, -20.7049, -13.2282, -5.75155, 1.72512, 9.20179]):
            seg.e_pas = value
        for seg, value in zip(self.apic[85], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[85], [0.000358131, 0.000384539, 0.000410948, 0.000437356, 0.000463765, 0.000490173, 0.000516582]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[85], [0.110753, 0.126598, 0.142443, 0.158288, 0.174133, 0.189978, 0.205824]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[81], [-49.0422, -43.2603, -37.4783, -31.6963, -25.9143]):
            seg.e_pas = value
        for seg, value in zip(self.apic[81], [0.570034, 0.189273, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[81], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[81], [0.000334281, 0.000354703, 0.000375126, 0.000395549, 0.000415971]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[81], [0.0868562, 0.0991098, 0.111363, 0.123617, 0.135871]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[83], [-19.4593, -12.3312, -5.20308, 1.92501, 9.0531]):
            seg.e_pas = value
        for seg, value in zip(self.apic[83], [0.000438771, 0.000463949, 0.000489126, 0.000514303, 0.000539481]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[83], [0.149551, 0.164657, 0.179763, 0.19487, 0.209976]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[82], [-19.4347, -12.2574, -5.0801, 2.09718, 9.27446]):
            seg.e_pas = value
        for seg, value in zip(self.apic[82], [0.000438858, 0.000464209, 0.00048956, 0.000514911, 0.000540262]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[82], [0.149603, 0.164813, 0.180024, 0.195235, 0.210445]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[80], [-63.3902, -62.6022, -61.8143, -61.0264, -60.2384, -59.4505, -58.6625, -57.8746, -57.0867]):
            seg.e_pas = value
        for seg, value in zip(self.apic[80], [0.39942, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[80], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[80], [0.000356187, 0.000384018, 0.000411848, 0.000439679, 0.00046751, 0.000495341, 0.000523172, 0.000551003, 0.000578834]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[80], [0.0912373, 0.107936, 0.124634, 0.141333, 0.158031, 0.17473, 0.191429, 0.208127, 0.224826]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[72], [-63.337, -62.5615, -61.7861, -61.0106, -60.2352, -59.4597, -58.6843, -57.9088, -57.1334, -56.3579, -55.5825, -54.807, -54.0316]):
            seg.e_pas = value
        for seg, value in zip(self.apic[72], [0.389828, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[72], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[72], [0.000439109, 0.000466499, 0.000493889, 0.000521278, 0.000548668, 0.000576058, 0.000603448, 0.000630837, 0.000658227, 0.000685617, 0.000713007, 0.000740396, 0.000767786]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[72], [0.107822, 0.124256, 0.14069, 0.157123, 0.173557, 0.189991, 0.206425, 0.222859, 0.239293, 0.255726, 0.27216, 0.288594, 0.305028]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[79], [-40.8094, -34.8915, -28.9735, -23.0555, -17.1375, -11.2195, -5.30156]):
            seg.e_pas = value
        for seg, value in zip(self.apic[79], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[79], [0.000415012, 0.000435915, 0.000456818, 0.000477721, 0.000498624, 0.000519527, 0.00054043]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[79], [0.114155, 0.126697, 0.139239, 0.15178, 0.164322, 0.176864, 0.189406]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[78], [-40.505, -33.9781, -27.4513, -20.9244, -14.3975, -7.87069, -1.34382]):
            seg.e_pas = value
        for seg, value in zip(self.apic[78], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[78], [0.000416087, 0.000439141, 0.000462194, 0.000485248, 0.000508302, 0.000531355, 0.000554409]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[78], [0.1148, 0.128632, 0.142465, 0.156297, 0.170129, 0.183961, 0.197793]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[76], [-61.6169, -61.0032, -60.3896, -59.776, -59.1624, -58.5488, -57.9352, -57.3216, -56.7079]):
            seg.e_pas = value
        for seg, value in zip(self.apic[76], [0.229052, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[76], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[76], [0.000449064, 0.000470738, 0.000492411, 0.000514085, 0.000535759, 0.000557432, 0.000579106, 0.000600779, 0.000622453]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[76], [0.134587, 0.147591, 0.160595, 0.173599, 0.186603, 0.199607, 0.212611, 0.225616, 0.23862]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[75], [-61.583, -60.9017, -60.2204, -59.5391, -58.8577, -58.1764, -57.4951, -56.8138, -56.1325]):
            seg.e_pas = value
        for seg, value in zip(self.apic[75], [0.267451, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[75], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[75], [0.00045026, 0.000474325, 0.00049839, 0.000522455, 0.00054652, 0.000570585, 0.000594649, 0.000618714, 0.000642779]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[75], [0.135304, 0.149743, 0.164182, 0.178621, 0.19306, 0.207499, 0.221938, 0.236377, 0.250816]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[71], [-62.4977, -61.6912, -60.8847, -60.0782, -59.2717]):
            seg.e_pas = value
        for seg, value in zip(self.apic[71], [0.000480597, 0.000509083, 0.000537569, 0.000566056, 0.000594542]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[71], [0.127867, 0.144959, 0.162051, 0.179143, 0.196234]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[70], [-62.4807, -61.6402, -60.7998, -59.9593, -59.1188]):
            seg.e_pas = value
        for seg, value in zip(self.apic[70], [0.000481197, 0.000510883, 0.00054057, 0.000570256, 0.000599942]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[70], [0.128227, 0.146039, 0.163851, 0.181663, 0.199475]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[68], [-63.3167, -62.5531, -61.7896, -61.026, -60.2625, -59.4989, -58.7354, -57.9718, -57.2083, -56.4447, -55.6812]):
            seg.e_pas = value
        for seg, value in zip(self.apic[68], [0.392068, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[68], [-65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652, -65.4652]):
            seg.ggk_cal = value
        for seg, value in zip(self.apic[68], [0.000470758, 0.000497727, 0.000524697, 0.000551666, 0.000578636, 0.000605605, 0.000632575, 0.000659544, 0.000686514, 0.000713483, 0.000740453]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[68], [0.114152, 0.130333, 0.146515, 0.162697, 0.178878, 0.19506, 0.211242, 0.227423, 0.243605, 0.259787, 0.275969]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[65], [-48.0893, -42.316, -36.5427]):
            seg.e_pas = value
        for seg, value in zip(self.apic[65], [0.520059, 0.201437, 0.2]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[65], [0.000482803, 0.000503195, 0.000523587]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[65], [0.116561, 0.128796, 0.141031]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[67], [-61.4855, -60.7251, -59.9648, -59.2045, -58.4442]):
            seg.e_pas = value
        for seg, value in zip(self.apic[67], [0.000547211, 0.000574066, 0.000600921, 0.000627776, 0.000654631]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[67], [0.155205, 0.171318, 0.187431, 0.203544, 0.219657]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[66], [-61.5235, -60.8393, -60.1551, -59.4709, -58.7867]):
            seg.e_pas = value
        for seg, value in zip(self.apic[66], [0.000545867, 0.000570034, 0.000594201, 0.000618368, 0.000642536]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[66], [0.154399, 0.168899, 0.183399, 0.1979, 0.2124]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[64], [-63.3013, -62.5438, -61.7862, -61.0287, -60.2711, -59.5136, -58.756, -57.9985, -57.2409, -56.4833, -55.7258]):
            seg.e_pas = value
        for seg, value in zip(self.apic[64], [0.427661, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[64], [0.000494668, 0.000521425, 0.000548183, 0.000574941, 0.000601698, 0.000628456, 0.000655214, 0.000681971, 0.000708729, 0.000735487, 0.000762244]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[64], [0.118934, 0.134988, 0.151043, 0.167097, 0.183152, 0.199207, 0.215261, 0.231316, 0.24737, 0.263425, 0.279479]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[63], [-63.2856, -62.5657, -61.8458, -61.1259, -60.406, -59.6862, -58.9663, -58.2464, -57.5265]):
            seg.e_pas = value
        for seg, value in zip(self.apic[63], [0.399057, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[63], [0.000519214, 0.000544641, 0.000570068, 0.000595495, 0.000620922, 0.000646349, 0.000671776, 0.000697203, 0.00072263]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[63], [0.123843, 0.139099, 0.154355, 0.169612, 0.184868, 0.200124, 0.21538, 0.230636, 0.245893]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[62], [-63.2677, -62.5052, -61.7427, -60.9801, -60.2176, -59.4551, -58.6925, -57.93, -57.1675, -56.4049, -55.6424]):
            seg.e_pas = value
        for seg, value in zip(self.apic[62], [0.400304, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[62], [0.000546999, 0.000573933, 0.000600867, 0.0006278, 0.000654734, 0.000681668, 0.000708601, 0.000735535, 0.000762469, 0.000789402, 0.000816336]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[62], [0.1294, 0.14556, 0.16172, 0.17788, 0.194041, 0.210201, 0.226361, 0.242521, 0.258681, 0.274842, 0.291002]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[61], [-63.2638, -62.6175, -61.9712, -61.3249, -60.6785, -60.0322, -59.3859]):
            seg.e_pas = value
        for seg, value in zip(self.apic[61], [0.389224, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[61], [0.000553094, 0.000575922, 0.000598751, 0.00062158, 0.000644409, 0.000667238, 0.000690066]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[61], [0.130619, 0.144316, 0.158013, 0.171711, 0.185408, 0.199105, 0.212802]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[60], [-63.2431, -62.5582, -61.8733, -61.1883, -60.5034, -59.8185, -59.1336, -58.4487, -57.7637, -57.0788, -56.3939]):
            seg.e_pas = value
        for seg, value in zip(self.apic[60], [0.367972, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[60], [0.000585414, 0.000609607, 0.000633799, 0.000657991, 0.000682183, 0.000706375, 0.000730567, 0.000754759, 0.000778951, 0.000803143, 0.000827336]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[60], [0.137083, 0.151598, 0.166113, 0.180629, 0.195144, 0.209659, 0.224174, 0.23869, 0.253205, 0.26772, 0.282236]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[59], [-63.2293, -62.5349, -61.8404, -61.146, -60.4515, -59.7571, -59.0626, -58.3682, -57.6737]):
            seg.e_pas = value
        for seg, value in zip(self.apic[59], [0.303296, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[59], [0.000606836, 0.000631365, 0.000655894, 0.000680423, 0.000704952, 0.000729481, 0.00075401, 0.000778539, 0.000803068]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[59], [0.141367, 0.156085, 0.170802, 0.185519, 0.200237, 0.214954, 0.229671, 0.244389, 0.259106]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[25], [-63.2209, -63.2068, -63.1927]):
            seg.e_pas = value
        for seg, value in zip(self.apic[25], [0.673625, 0.6, 0.6]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[25], [0.000620012, 0.000642002, 0.000663991]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[25], [0.144002, 0.1484, 0.152798]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[58], [-62.6072, -61.9214, -61.2357, -60.55, -59.8642, -59.1785, -58.4928]):
            seg.e_pas = value
        for seg, value in zip(self.apic[58], [0.000640325, 0.000664546, 0.000688767, 0.000712988, 0.000737209, 0.00076143, 0.00078565]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[58], [0.156749, 0.171281, 0.185814, 0.200346, 0.214879, 0.229411, 0.243944]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[57], [-62.6002, -61.9005, -61.2008, -60.5011, -59.8014]):
            seg.e_pas = value
        for seg, value in zip(self.apic[57], [0.000640572, 0.000665286, 0.00069, 0.000714715, 0.000739429]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[57], [0.156897, 0.171725, 0.186554, 0.201382, 0.216211]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[55], [-63.1785, -62.5484, -61.9183, -61.2882, -60.6582, -60.0281, -59.398, -58.7679, -58.1379]):
            seg.e_pas = value
        for seg, value in zip(self.apic[55], [0.264489, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[55], [0.000686113, 0.000708368, 0.000730623, 0.000752879, 0.000775134, 0.000797389, 0.000819644, 0.000841899, 0.000864154]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[55], [0.157223, 0.170576, 0.183929, 0.197282, 0.210635, 0.223988, 0.237341, 0.250694, 0.264047]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[54], [-63.1707, -62.4007, -61.6306, -60.8606, -60.0905]):
            seg.e_pas = value
        for seg, value in zip(self.apic[54], [0.337566, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[54], [0.000698189, 0.000725389, 0.000752588, 0.000779787, 0.000806986]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[54], [0.159638, 0.175957, 0.192277, 0.208596, 0.224916]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[53], [-63.14, -62.4581, -61.7763, -61.0944, -60.4125, -59.7306, -59.0487, -58.3668, -57.6849, -57.003, -56.3211]):
            seg.e_pas = value
        for seg, value in zip(self.apic[53], [0.295294, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[53], [0.00074601, 0.000770095, 0.000794181, 0.000818266, 0.000842352, 0.000866437, 0.000890522, 0.000914608, 0.000938693, 0.000962778, 0.000986864]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[53], [0.169202, 0.183653, 0.198104, 0.212556, 0.227007, 0.241458, 0.255909, 0.270361, 0.284812, 0.299263, 0.313714]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[48], [-63.1184, -63.1052, -63.0921, -63.0789, -63.0658, -63.0526, -63.0395]):
            seg.e_pas = value
        for seg, value in zip(self.apic[48], [0.308198, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[48], [0.000779772, 0.000800263, 0.000820753, 0.000841243, 0.000861733, 0.000882224, 0.000902714]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[48], [0.175954, 0.180053, 0.184151, 0.188249, 0.192347, 0.196445, 0.200543]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[50], [-63.0246, -63.008, -62.9913]):
            seg.e_pas = value
        for seg, value in zip(self.apic[50], [0.000925919, 0.000951837, 0.000977756]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[50], [0.205184, 0.210367, 0.215551]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[49], [-63.027, -63.0152, -63.0034, -62.9915, -62.9797]):
            seg.e_pas = value
        for seg, value in zip(self.apic[49], [0.000922173, 0.000940602, 0.00095903, 0.000977459, 0.000995887]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[49], [0.204435, 0.20812, 0.211806, 0.215492, 0.219177]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[47], [-63.1099, -63.0947, -63.0795, -63.0643, -63.0492, -63.034, -63.0188]):
            seg.e_pas = value
        for seg, value in zip(self.apic[47], [0.220026, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[47], [0.000793024, 0.000816684, 0.000840344, 0.000864005, 0.000887665, 0.000911326, 0.000934986]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[47], [0.178605, 0.183337, 0.188069, 0.192801, 0.197533, 0.202265, 0.206997]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[52], [-62.9755, -62.9603, -62.9452, -62.9301, -62.915, -62.8998, -62.8847, -62.8696, -62.8544, -62.8393, -62.8242]):
            seg.e_pas = value
        for seg, value in zip(self.apic[52], [0.0010025, 0.00102608, 0.00104966, 0.00107324, 0.00109682, 0.0011204, 0.00114398, 0.00116755, 0.00119113, 0.00121471, 0.00123829]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[52], [0.220501, 0.225217, 0.229932, 0.234648, 0.239364, 0.24408, 0.248795, 0.253511, 0.258227, 0.262942, 0.267658]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[51], [-62.9749, -62.9586, -62.9424, -62.9261, -62.9098, -62.8935, -62.8773, -62.861, -62.8447, -62.8285, -62.8122]):
            seg.e_pas = value
        for seg, value in zip(self.apic[51], [0.00100339, 0.00102875, 0.00105411, 0.00107947, 0.00110482, 0.00113018, 0.00115554, 0.0011809, 0.00120626, 0.00123161, 0.00125697]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[51], [0.220679, 0.22575, 0.230822, 0.235893, 0.240965, 0.246037, 0.251108, 0.25618, 0.261251, 0.266323, 0.271394]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[40], [-63.098, -63.0829, -63.0679, -63.0529, -63.0378]):
            seg.e_pas = value
        for seg, value in zip(self.apic[40], [0.351242, 0.2, 0.2, 0.2, 0.2]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[40], [0.0008116, 0.00083503, 0.000858461, 0.000881891, 0.000905322]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[40], [0.18232, 0.187006, 0.191692, 0.196378, 0.201064]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[44], [-63.0243, -63.0122, -63.0001, -62.988, -62.9759]):
            seg.e_pas = value
        for seg, value in zip(self.apic[44], [0.163267, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[44], [0.000926466, 0.000945322, 0.000964179, 0.000983035, 0.00100189]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[44], [0.205293, 0.209064, 0.212836, 0.216607, 0.220378]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[41], [-63.0228, -63.0079, -62.9929, -62.9779, -62.963, -62.948, -62.9331, -62.9181, -62.9031, -62.8882, -62.8732]):
            seg.e_pas = value
        for seg, value in zip(self.apic[41], [0.170262, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[41], [0.000928697, 0.000952016, 0.000975335, 0.000998654, 0.00102197, 0.00104529, 0.00106861, 0.00109193, 0.00111525, 0.00113857, 0.00116189]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[41], [0.205739, 0.210403, 0.215067, 0.219731, 0.224395, 0.229058, 0.233722, 0.238386, 0.24305, 0.247714, 0.252377]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[37], [-63.0694, -63.0569, -63.0444, -63.032, -63.0195]):
            seg.e_pas = value
        for seg, value in zip(self.apic[37], [0.250084, 0.15, 0.15, 0.15, 0.15]):
            seg.depth_cacum = value
        for seg, value in zip(self.apic[37], [0.000856171, 0.000875596, 0.00089502, 0.000914445, 0.000933869]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[37], [0.191234, 0.195119, 0.199004, 0.202889, 0.206774]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[46], [-62.9616, -62.9453, -62.929, -62.9126, -62.8963]):
            seg.e_pas = value
        for seg, value in zip(self.apic[46], [0.00102405, 0.00104951, 0.00107497, 0.00110043, 0.00112589]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[46], [0.22481, 0.229902, 0.234994, 0.240087, 0.245179]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[43], [-62.8588, -62.8451, -62.8313, -62.8175, -62.8038, -62.79, -62.7762]):
            seg.e_pas = value
        for seg, value in zip(self.apic[43], [0.00118427, 0.00120573, 0.00122719, 0.00124864, 0.0012701, 0.00129155, 0.00131301]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[43], [0.256855, 0.261146, 0.265437, 0.269729, 0.27402, 0.278311, 0.282602]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[42], [-62.8579, -62.8421, -62.8264, -62.8106, -62.7949]):
            seg.e_pas = value
        for seg, value in zip(self.apic[42], [0.00118581, 0.00121035, 0.00123488, 0.00125942, 0.00128395]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[42], [0.257163, 0.26207, 0.266977, 0.271884, 0.276791]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[39], [-63.006, -62.9915, -62.9769, -62.9624, -62.9478, -62.9333, -62.9187, -62.9042, -62.8896, -62.8751, -62.8605]):
            seg.e_pas = value
        for seg, value in zip(self.apic[39], [0.000954918, 0.000977592, 0.00100027, 0.00102294, 0.00104561, 0.00106829, 0.00109096, 0.00111363, 0.00113631, 0.00115898, 0.00118165]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[39], [0.210984, 0.215518, 0.220053, 0.224588, 0.229123, 0.233657, 0.238192, 0.242727, 0.247261, 0.251796, 0.256331]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[38], [-63.0051, -62.9888, -62.9726, -62.9563, -62.94, -62.9237, -62.9074, -62.8911, -62.8748, -62.8586, -62.8423]):
            seg.e_pas = value
        for seg, value in zip(self.apic[38], [0.000956273, 0.000981655, 0.00100704, 0.00103242, 0.0010578, 0.00108318, 0.00110857, 0.00113395, 0.00115933, 0.00118471, 0.0012101]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[38], [0.211255, 0.216331, 0.221407, 0.226484, 0.23156, 0.236637, 0.241713, 0.24679, 0.251866, 0.256943, 0.262019]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[36], [-63.0487, -63.0324, -63.016, -62.9997, -62.9834, -62.967, -62.9507, -62.9343, -62.918, -62.9016, -62.8853, -62.8689, -62.8526]):
            seg.e_pas = value
        for seg, value in zip(self.apic[36], [0.000888314, 0.00091379, 0.000939266, 0.000964742, 0.000990218, 0.00101569, 0.00104117, 0.00106665, 0.00109212, 0.0011176, 0.00114307, 0.00116855, 0.00119403]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[36], [0.197663, 0.202758, 0.207853, 0.212948, 0.218044, 0.223139, 0.228234, 0.233329, 0.238424, 0.243519, 0.248615, 0.25371, 0.258805]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[33], [-63.0499, -63.0359, -63.0219, -63.0079, -62.9939, -62.9799, -62.966]):
            seg.e_pas = value
        for seg, value in zip(self.apic[33], [0.000886481, 0.00090829, 0.0009301, 0.000951909, 0.000973718, 0.000995528, 0.00101734]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[33], [0.197296, 0.201658, 0.20602, 0.210382, 0.214744, 0.219106, 0.223467]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[35], [-62.9504, -62.9334, -62.9164, -62.8994, -62.8824]):
            seg.e_pas = value
        for seg, value in zip(self.apic[35], [0.0010415, 0.00106802, 0.00109455, 0.00112107, 0.00114759]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[35], [0.2283, 0.233605, 0.238909, 0.244213, 0.249518]):
            seg.gkabar_kad = value
        for seg, value in zip(self.apic[34], [-62.9506, -62.9339, -62.9172, -62.9005, -62.8838]):
            seg.e_pas = value
        for seg, value in zip(self.apic[34], [0.00104125, 0.00106727, 0.00109329, 0.00111932, 0.00114534]):
            seg.ghdbar_hd = value
        for seg, value in zip(self.apic[34], [0.22825, 0.233455, 0.238659, 0.243863, 0.249067]):
            seg.gkabar_kad = value
    
    def _create_sections(self):
        from neuron import h
        self.soma = h.Section(cell=self, name="soma")
        self.axon = h.Section(cell=self, name="axon")
        self.apic = [h.Section(cell=self, name="apic[%d]" % i) for i in range(134)]
        self.basal = [h.Section(cell=self, name="basal[%d]" % i) for i in range(58)]
    
    def _shape_sections(self):
        self._set_section_morphology(self.apic[0], [[0.0, 0.0, 0.0, 3.7], [10.413, 0.518, -0.405, 3.7], [19.018, -0.622, -0.813, 3.2], [30.334, -1.57, -1.549, 2.7], [39.121, -2.245, -2.457, 2.7]])
        self._set_section_morphology(self.apic[100], [[159.072, -14.874, -1.271, 0.3], [166.559, -15.116, 1.244, 0.3], [174.046, -15.358, 3.758, 0.3], [174.046, -15.358, 3.758, 0.3], [175.829, -15.416, 4.357, 0.3], [188.571, -14.478, 9.888, 0.3], [188.571, -14.478, 9.888, 0.3], [189.373, -14.419, 10.236, 0.3], [202.272, -14.276, 14.089, 0.3], [203.542, -14.338, 14.815, 0.3], [203.542, -14.338, 14.815, 0.3], [212.21, -14.765, 19.768, 0.3], [217.368, -14.026, 22.34, 0.3], [217.368, -14.026, 22.34, 0.3], [225.989, -12.791, 26.641, 0.3], [231.112, -12.626, 29.93, 0.3], [231.112, -12.626, 29.93, 0.3], [238.149, -12.4, 34.449, 0.3], [244.978, -13.491, 37.186, 0.3], [244.978, -13.491, 37.186, 0.3], [251.776, -14.577, 39.91, 0.3], [259.356, -13.767, 43.436, 0.3], [259.356, -13.767, 43.436, 0.3], [261.755, -13.51, 44.551, 0.3], [264.963, -9.267, 47.666, 0.3], [265.674, -2.674, 49.85, 0.3], [265.674, -2.674, 49.85, 0.3], [265.894, -0.638, 50.524, 0.3], [269.82, 12.286, 52.472, 0.3], [269.82, 12.286, 52.472, 0.3]])
        self._set_section_morphology(self.apic[101], [[159.072, -14.874, -1.271, 0.3], [162.932, -11.885, 1.918, 0.3], [165.361, -5.916, 6.642, 0.3], [165.361, -5.916, 6.642, 0.3], [165.776, -4.897, 7.448, 0.3], [164.045, -5.906, 12.371, 0.3], [163.126, -2.45, 18.241, 0.3], [163.025, -2.275, 18.42, 0.3], [163.025, -2.275, 18.42, 0.3], [161.268, 0.769, 21.549, 0.3], [162.717, 4.52, 25.061, 0.3], [160.316, 7.041, 26.524, 0.3], [160.316, 7.041, 26.524, 0.3], [156.995, 10.529, 28.547, 0.3], [154.766, 14.924, 34.809, 0.3], [154.534, 15.127, 35.358, 0.3], [154.534, 15.127, 35.358, 0.3], [151.903, 17.424, 41.577, 0.3], [145.77, 19.885, 42.617, 0.3]])
        self._set_section_morphology(self.apic[102], [[112.245, -21.105, -5.704, 2.2], [114.319, -17.027, -2.159, 0.6], [120.896, -12.781, 5.188, 0.6], [124.147, -13.268, 8.922, 0.6]])
        self._set_section_morphology(self.apic[103], [[124.147, -13.268, 8.922, 0.6], [125.597, -12.407, 10.751, 0.6], [127.047, -11.547, 12.58, 0.6]])
        self._set_section_morphology(self.apic[104], [[127.047, -11.547, 12.58, 0.6], [131.686, -10.365, 18.871, 0.3], [138.187, -9.509, 25.701, 0.3], [138.187, -9.509, 25.701, 0.3], [138.788, -9.43, 26.333, 0.3], [144.611, -4.958, 30.617, 0.3], [151.834, -3.501, 33.725, 0.3], [151.834, -3.501, 33.725, 0.3], [152.752, -3.316, 34.12, 0.3], [160.435, -4.674, 38.167, 0.3], [167.71, -4.882, 40.239, 0.3], [167.71, -4.882, 40.239, 0.3], [169.619, -4.937, 40.783, 0.3], [176.175, -4.891, 44.722, 0.3], [183.087, -5.511, 48.148, 0.3], [183.087, -5.511, 48.148, 0.3], [185.552, -5.732, 49.37, 0.3], [190.099, -6.619, 55.204, 0.3], [195.318, -7.729, 58.081, 0.3], [196.06, -7.731, 58.896, 0.3], [196.06, -7.731, 58.896, 0.3], [198.719, -7.738, 61.814, 0.3], [207.689, -4.78, 66.843, 0.3], [209.892, -5.263, 68.372, 0.3], [209.892, -5.263, 68.372, 0.3], [213.319, -6.015, 70.752, 0.3], [219.349, -2.658, 74.576, 0.3], [223.091, -0.158, 77.267, 0.3]])
        self._set_section_morphology(self.apic[105], [[127.047, -11.547, 12.58, 0.6], [130.015, -6.176, 16.653, 0.3], [134.377, -1.243, 21.331, 0.3], [134.333, -0.289, 21.754, 0.3], [134.333, -0.289, 21.754, 0.3], [134.08, 5.152, 24.163, 0.3], [130.962, 12.433, 26.286, 0.3], [129.621, 14.211, 26.977, 0.3], [129.621, 14.211, 26.977, 0.3], [125.248, 20.011, 29.233, 0.3], [119.979, 27.148, 29.664, 0.3], [119.979, 27.148, 29.664, 0.3], [119.699, 27.528, 29.687, 0.3], [118.008, 34.36, 31.915, 0.3], [117.944, 38.058, 34.327, 0.3], [119.797, 40.901, 36.83, 0.3], [119.797, 40.901, 36.83, 0.3], [121.355, 43.292, 38.934, 0.3], [123.123, 48.521, 44.437, 0.3], [122.917, 53.312, 46.311, 0.3]])
        self._set_section_morphology(self.apic[106], [[124.147, -13.268, 8.922, 0.6], [131.953, -16.242, 11.513, 0.3], [137.84, -17.839, 13.621, 0.3], [137.84, -17.839, 13.621, 0.3], [144.243, -19.574, 15.912, 0.3], [151.816, -20.896, 18.712, 0.3], [151.816, -20.896, 18.712, 0.3], [159.297, -22.201, 21.479, 0.3], [164.685, -25.416, 24.838, 0.3], [164.685, -25.416, 24.838, 0.3], [164.834, -25.505, 24.931, 0.3], [172.208, -29.385, 29.521, 0.3], [176.674, -30.502, 32.512, 0.3], [176.674, -30.502, 32.512, 0.3], [180.594, -31.482, 35.137, 0.3], [185.531, -33.02, 40.01, 0.3], [188.196, -33.687, 41.795, 0.3], [188.196, -33.687, 41.795, 0.3], [193.917, -35.118, 45.626, 0.3], [201.259, -37.05, 48.636, 0.3], [201.259, -37.05, 48.636, 0.3], [204.304, -37.851, 49.885, 0.3], [214.455, -42.587, 53.635, 0.3], [214.455, -42.587, 53.635, 0.3], [214.598, -42.653, 53.687, 0.3], [224.051, -48.236, 58.456, 0.3], [226.87, -48.914, 59.448, 0.3], [226.87, -48.914, 59.448, 0.3], [231.206, -49.957, 60.974, 0.3], [241.356, -49.854, 63.606, 0.3], [241.356, -49.854, 63.606, 0.3], [244.138, -49.825, 64.328, 0.3], [250.96, -52.488, 67.348, 0.3], [254.941, -53.024, 69.155, 0.3], [254.941, -53.024, 69.155, 0.3], [262.684, -54.066, 72.669, 0.3], [268.862, -53.907, 75.077, 0.3], [268.862, -53.907, 75.077, 0.3]])
        self._set_section_morphology(self.apic[107], [[89.57, -14.481, -4.853, 2.2], [94.622, -9.803, -10.649, 0.3], [100.241, -6.775, -11.271, 0.3], [100.241, -6.775, -11.271, 0.3], [109.961, -1.537, -12.347, 0.3], [114.141, -0.747, -13.1, 0.3], [114.141, -0.747, -13.1, 0.3], [122.427, 0.818, -14.592, 0.3], [128.98, 2.809, -14.738, 0.3], [128.98, 2.809, -14.738, 0.3], [141.056, 6.479, -15.008, 0.3], [143.728, 7.268, -15.148, 0.3], [143.728, 7.268, -15.148, 0.3], [151.11, 9.446, -15.536, 0.3], [158.492, 11.625, -15.924, 0.3], [158.492, 11.625, -15.924, 0.3], [159.091, 11.802, -15.955, 0.3], [170.951, 14.354, -16.24, 0.3], [173.51, 13.708, -16.517, 0.3], [173.51, 13.708, -16.517, 0.3], [179.288, 12.248, -17.143, 0.3], [188.632, 11.07, -16.921, 0.3], [188.632, 11.07, -16.921, 0.3], [190.388, 10.849, -16.879, 0.3], [204.002, 11.631, -16.443, 0.3], [204.002, 11.631, -16.443, 0.3], [205.871, 11.738, -16.383, 0.3], [219.203, 14.084, -16.044, 0.3], [219.203, 14.084, -16.044, 0.3], [219.751, 14.181, -16.03, 0.3], [230.82, 24.048, -15.117, 0.3], [230.82, 24.048, -15.117, 0.3], [232.79, 25.803, -14.955, 0.3], [238.058, 27.818, -13.655, 0.3], [245.027, 28.243, -13.708, 0.3], [245.027, 28.243, -13.708, 0.3]])
        self._set_section_morphology(self.apic[108], [[68.765, -8.444, -3.362, 2.2], [69.379, -13.864, 0.82, 0.3], [69.543, -14.304, 2.062, 0.3], [69.543, -14.304, 2.062, 0.3], [70.254, -16.212, 7.451, 0.3], [68.62, -16.964, 9.1, 0.3], [68.62, -16.964, 9.1, 0.3], [65.543, -18.38, 12.207, 0.3], [64.745, -20.215, 15.206, 0.3]])
        self._set_section_morphology(self.apic[109], [[64.745, -20.215, 15.206, 0.3], [68.415, -25.543, 21.091, 0.3], [67.754, -26.846, 22.206, 0.3], [67.754, -26.846, 22.206, 0.3], [66.357, -29.6, 24.564, 0.3], [62.401, -31.681, 29.553, 0.3], [62.401, -31.681, 29.553, 0.3], [61.398, -32.208, 30.817, 0.3], [57.639, -34.676, 35.642, 0.3], [55.52, -34.529, 36.502, 0.3]])
        self._set_section_morphology(self.apic[10], [[159.496, -38.626, -8.682, 1.8], [160.347, -39.421, -9.359, 1.8], [161.197, -40.215, -10.035, 1.8]])
        self._set_section_morphology(self.apic[110], [[55.52, -34.529, 36.502, 0.3], [56.768, -38.054, 40.178, 0.3], [58.534, -43.873, 42.116, 0.3], [58.534, -43.873, 42.116, 0.3], [60.986, -51.948, 44.805, 0.3], [61.308, -54.417, 46.02, 0.3], [61.308, -54.417, 46.02, 0.3], [61.841, -58.496, 48.029, 0.3], [65.962, -63.737, 50.317, 0.3], [65.962, -63.737, 50.317, 0.3], [66.216, -64.06, 50.458, 0.3], [72.735, -68.181, 58.506, 0.3], [72.755, -68.218, 58.524, 0.3], [72.755, -68.218, 58.524, 0.3], [75.292, -72.926, 60.803, 0.3], [77.83, -77.634, 63.082, 0.3]])
        self._set_section_morphology(self.apic[111], [[55.52, -34.529, 36.502, 0.3], [51.695, -33.856, 34.228, 0.3], [46.421, -36.742, 37.121, 0.3], [46.421, -36.742, 37.121, 0.3], [45.022, -37.507, 37.888, 0.3], [38.094, -39.372, 43.965, 0.3], [38.094, -39.372, 43.965, 0.3], [36.992, -39.669, 44.931, 0.3], [35.314, -40.165, 51.348, 0.3], [33.407, -41.167, 53.472, 0.3], [33.407, -41.167, 53.472, 0.3], [29.728, -43.1, 57.569, 0.3], [30.5, -47.765, 60.044, 0.3], [30.5, -47.765, 60.044, 0.3], [30.733, -49.171, 60.79, 0.3], [32.66, -48.181, 67.409, 0.3], [32.821, -48.747, 69.94, 0.3]])
        self._set_section_morphology(self.apic[112], [[64.745, -20.215, 15.206, 0.3], [52.28, -18.895, 18.865, 0.3], [49.865, -18.478, 19.025, 0.3], [49.865, -18.478, 19.025, 0.3], [41.265, -16.993, 19.597, 0.3], [35.623, -13.388, 20.59, 0.3], [35.623, -13.388, 20.59, 0.3], [31.535, -10.776, 21.311, 0.3], [29.803, -5.5, 24.576, 0.3], [27.806, -2.271, 26.294, 0.3], [27.806, -2.271, 26.294, 0.3], [26.169, 0.375, 27.702, 0.3], [28.262, 4.978, 33.241, 0.3], [30.741, 7.867, 33.334, 0.3], [30.707, 8.647, 33.459, 0.3], [30.707, 8.647, 33.459, 0.3], [30.285, 18.502, 35.049, 0.3], [31.905, 23.76, 35.528, 0.3]])
        self._set_section_morphology(self.apic[113], [[55.455, -5.292, -1.809, 2.2], [58.858, 1.488, -4.758, 0.3], [58.627, 7.859, -2.924, 0.3]])
        self._set_section_morphology(self.apic[114], [[58.627, 7.859, -2.924, 0.3], [62.765, 10.771, 3.292, 0.3], [64.982, 13.758, 7.375, 0.3], [68.716, 14.69, 10.605, 0.3]])
        self._set_section_morphology(self.apic[115], [[68.716, 14.69, 10.605, 0.3], [69.898, 11.189, 15.28, 0.3], [73.807, 11.018, 18.549, 0.3]])
        self._set_section_morphology(self.apic[116], [[73.807, 11.018, 18.549, 0.3], [72.812, 9.256, 24.541, 0.3], [73.05, 7.624, 28.606, 0.3], [72.111, 8.034, 29.59, 0.3], [72.111, 8.034, 29.59, 0.3], [68.59, 9.57, 33.277, 0.3], [65.055, 9.124, 36.564, 0.3], [63.333, 9.12, 37.502, 0.3], [63.333, 9.12, 37.502, 0.3], [61.769, 9.117, 38.353, 0.3], [55.423, 8.515, 43.464, 0.3], [55.08, 7.907, 45.531, 0.3], [55.08, 7.907, 45.531, 0.3], [54.428, 6.753, 49.456, 0.3], [52.809, 8.339, 56.829, 0.3], [52.825, 8.58, 56.965, 0.3], [52.825, 8.58, 56.965, 0.3], [53.34, 16.051, 61.187, 0.3], [52.533, 18.934, 63.068, 0.3]])
        self._set_section_morphology(self.apic[117], [[73.807, 11.018, 18.549, 0.3], [79.385, 9.269, 20.963, 0.3], [83.579, 6.915, 25.307, 0.3], [85.868, 7.808, 27.229, 0.3], [85.868, 7.808, 27.229, 0.3], [92.535, 10.411, 32.828, 0.3], [97.856, 12.123, 36.765, 0.3], [97.856, 12.123, 36.765, 0.3], [99.151, 12.539, 37.723, 0.3], [97.012, 15.329, 43.027, 0.3], [93.829, 16.35, 47.805, 0.3], [95.321, 15.885, 49.158, 0.3], [95.321, 15.885, 49.158, 0.3], [101.047, 14.099, 54.35, 0.3], [107.956, 13.571, 58.332, 0.3], [107.956, 13.571, 58.332, 0.3], [109.916, 13.42, 59.461, 0.3], [112.108, 17.987, 63.504, 0.3], [116.385, 22.419, 67.186, 0.3]])
        self._set_section_morphology(self.apic[118], [[68.716, 14.69, 10.605, 0.3], [71.572, 17.465, 12.229, 0.3], [76.06, 27.742, 12.274, 0.3], [76.06, 27.742, 12.274, 0.3], [77.207, 30.369, 12.285, 0.3], [80.166, 40.456, 15.241, 0.3], [80.694, 41.99, 15.836, 0.3], [80.694, 41.99, 15.836, 0.3], [83.267, 49.452, 18.734, 0.3], [86.136, 55.834, 19.977, 0.3], [86.136, 55.834, 19.977, 0.3], [88.019, 60.02, 20.793, 0.3], [89.396, 62.732, 20.818, 0.3], [94.926, 68.206, 21.508, 0.3], [94.926, 68.206, 21.508, 0.3], [95.424, 68.699, 21.57, 0.3], [105.738, 74.381, 27.122, 0.3], [107.136, 75.318, 27.739, 0.3], [107.136, 75.318, 27.739, 0.3], [112.134, 78.667, 29.945, 0.3], [113.949, 83.347, 32.456, 0.3], [113.881, 86.664, 33.551, 0.3], [113.881, 86.664, 33.551, 0.3], [113.777, 91.799, 35.246, 0.3], [116.215, 93.132, 36.376, 0.3], [119.313, 94.779, 37.041, 0.3], [121.177, 96.299, 39.633, 0.3]])
        self._set_section_morphology(self.apic[119], [[58.627, 7.859, -2.924, 0.3], [58.859, 14.022, -2.879, 0.3], [59.091, 20.186, -2.833, 0.3], [59.091, 20.186, -2.833, 0.3], [59.271, 24.956, -2.798, 0.3], [59.901, 32.488, -2.53, 0.3], [59.901, 32.488, -2.53, 0.3], [60.415, 38.632, -2.311, 0.3], [60.928, 44.775, -2.093, 0.3], [60.928, 44.775, -2.093, 0.3], [61.578, 52.542, -1.816, 0.3], [62.007, 57.059, -1.764, 0.3], [62.007, 57.059, -1.764, 0.3], [62.59, 63.199, -1.692, 0.3], [63.174, 69.339, -1.62, 0.3]])
        self._set_section_morphology(self.apic[11], [[161.197, -40.215, -10.035, 1.8], [169.834, -41.368, -10.942, 1.6], [174.742, -42.389, -10.594, 1.6]])
        self._set_section_morphology(self.apic[120], [[63.174, 69.339, -1.62, 0.3], [68.506, 73.314, -0.192, 0.3], [73.839, 77.289, 1.236, 0.3], [73.839, 77.289, 1.236, 0.3], [74.553, 77.822, 1.428, 0.3], [83.588, 86.439, 3.717, 0.3], [83.588, 86.439, 3.717, 0.3], [84.063, 86.892, 3.837, 0.3], [89.653, 98.56, 3.92, 0.3], [89.653, 98.56, 3.92, 0.3], [91.701, 102.834, 3.951, 0.3], [97.344, 109.48, 5.559, 0.3], [97.344, 109.48, 5.559, 0.3], [99.784, 112.353, 6.255, 0.3], [103.517, 119.57, 7.828, 0.3], [104.373, 120.712, 8.278, 0.3], [104.373, 120.712, 8.278, 0.3], [108.611, 126.363, 10.504, 0.3], [114.055, 128.685, 12.347, 0.3], [114.055, 128.685, 12.347, 0.3], [115.692, 129.383, 12.901, 0.3], [120.911, 128.273, 15.778, 0.3], [125.638, 130.462, 18.04, 0.3]])
        self._set_section_morphology(self.apic[121], [[63.174, 69.339, -1.62, 0.3], [65.807, 83.169, -6.797, 0.3], [65.852, 84.159, -7.093, 0.3], [65.852, 84.159, -7.093, 0.3], [66.305, 94.009, -10.036, 0.3], [66.743, 99.486, -11.709, 0.3], [66.743, 99.486, -11.709, 0.3], [67.286, 106.268, -13.78, 0.3], [69.985, 114.026, -17.262, 0.3], [69.985, 114.026, -17.262, 0.3], [70.404, 115.231, -17.803, 0.3], [76.513, 124.311, -19.127, 0.3], [79.223, 126.667, -19.62, 0.3], [79.223, 126.667, -19.62, 0.3], [85.358, 132.002, -20.737, 0.3], [89.581, 138.532, -21.621, 0.3]])
        self._set_section_morphology(self.apic[122], [[39.121, -2.245, -2.457, 2.7], [41.166, 0.765, -6.657, 1.5], [43.211, 3.775, -10.856, 0.3]])
        self._set_section_morphology(self.apic[123], [[43.211, 3.775, -10.856, 0.3], [45.779, 11.344, -13.378, 0.3], [49.079, 13.436, -13.711, 0.3], [49.079, 13.436, -13.711, 0.3], [55.719, 17.645, -14.382, 0.3], [59.344, 20.156, -14.204, 0.3], [59.344, 20.156, -14.204, 0.3], [65.084, 24.132, -13.924, 0.3], [69.617, 26.898, -13.693, 0.3]])
        self._set_section_morphology(self.apic[124], [[69.617, 26.898, -13.693, 0.3], [74.729, 28.068, -14.938, 0.3], [79.841, 29.237, -16.183, 0.3], [79.841, 29.237, -16.183, 0.3], [81.165, 29.54, -16.506, 0.3], [90.149, 31.903, -17.836, 0.3], [90.149, 31.903, -17.836, 0.3], [95.66, 33.352, -18.652, 0.3], [100.608, 33.887, -19.342, 0.3]])
        self._set_section_morphology(self.apic[125], [[100.608, 33.887, -19.342, 0.3], [113.208, 29.908, -21.924, 0.3], [113.964, 29.669, -22.032, 0.3], [113.964, 29.669, -22.032, 0.3], [124.79, 26.252, -23.578, 0.3], [127.54, 26.339, -24.13, 0.3], [127.54, 26.339, -24.13, 0.3], [132.333, 26.491, -25.093, 0.3], [141.369, 26.256, -27.5, 0.3], [141.387, 26.259, -27.503, 0.3], [141.387, 26.259, -27.503, 0.3], [149.363, 27.925, -29.019, 0.3], [154.165, 29.549, -32.183, 0.3], [154.165, 29.549, -32.183, 0.3], [154.96, 29.818, -32.707, 0.3], [162.376, 34.284, -35.836, 0.3], [166.057, 34.298, -37.569, 0.3], [166.057, 34.298, -37.569, 0.3], [168.916, 34.309, -38.915, 0.3], [179.424, 31.422, -41.045, 0.3], [179.424, 31.422, -41.045, 0.3], [181.666, 30.806, -41.499, 0.3], [192.318, 28.48, -46.254, 0.3]])
        self._set_section_morphology(self.apic[126], [[100.608, 33.887, -19.342, 0.3], [106.066, 35.007, -18.671, 0.3], [111.525, 36.127, -18.0, 0.3], [111.525, 36.127, -18.0, 0.3], [116.744, 37.198, -17.358, 0.3], [122.295, 39.011, -17.823, 0.3], [122.295, 39.011, -17.823, 0.3], [127.359, 40.665, -18.248, 0.3], [132.377, 43.589, -17.327, 0.3], [132.377, 43.589, -17.327, 0.3], [134.956, 45.091, -16.853, 0.3], [140.673, 50.911, -17.713, 0.3], [140.673, 50.911, -17.713, 0.3], [142.818, 53.095, -18.035, 0.3], [144.553, 55.167, -18.473, 0.3], [144.12, 60.547, -18.131, 0.3]])
        self._set_section_morphology(self.apic[127], [[69.617, 26.898, -13.693, 0.3], [74.153, 37.013, -10.634, 0.3], [75.371, 40.18, -9.245, 0.3], [75.371, 40.18, -9.245, 0.3], [78.115, 47.315, -6.114, 0.3], [82.041, 52.866, -4.91, 0.3], [82.041, 52.866, -4.91, 0.3], [83.576, 55.036, -4.439, 0.3], [91.191, 59.988, -1.051, 0.3], [93.095, 61.928, -0.511, 0.3], [93.095, 61.928, -0.511, 0.3], [99.449, 68.404, 1.292, 0.3], [101.957, 73.559, 2.751, 0.3], [101.957, 73.559, 2.751, 0.3], [104.761, 79.323, 4.382, 0.3], [105.528, 87.829, 4.822, 0.3], [105.528, 87.829, 4.822, 0.3], [106.049, 93.599, 5.121, 0.3], [106.392, 102.942, 5.647, 0.3], [106.392, 102.942, 5.647, 0.3], [106.753, 112.778, 6.202, 0.3], [106.843, 118.009, 5.306, 0.3], [106.843, 118.009, 5.306, 0.3], [106.869, 119.552, 5.042, 0.3], [102.845, 132.293, 2.505, 0.3], [102.845, 132.293, 2.505, 0.3], [101.725, 135.84, 1.799, 0.3], [103.768, 146.72, -0.838, 0.3], [103.768, 146.72, -0.838, 0.3]])
        self._set_section_morphology(self.apic[128], [[43.211, 3.775, -10.856, 0.3], [40.34, 4.653, -18.084, 0.3], [42.466, 6.418, -25.999, 0.3], [42.466, 6.418, -25.999, 0.3], [42.601, 6.531, -26.502, 0.3], [47.845, 6.956, -31.681, 0.3], [49.583, 9.534, -37.143, 0.3], [50.607, 9.393, -38.867, 0.3], [50.607, 9.393, -38.867, 0.3], [52.441, 9.14, -41.957, 0.3], [55.981, 13.766, -48.854, 0.3], [56.216, 13.678, -52.425, 0.3], [56.216, 13.678, -52.425, 0.3], [56.736, 13.485, -60.326, 0.3], [55.358, 13.89, -68.447, 0.3], [55.365, 13.921, -68.476, 0.3], [55.365, 13.921, -68.476, 0.3], [56.754, 20.242, -74.525, 0.3], [57.945, 22.407, -81.448, 0.3], [57.945, 22.407, -81.448, 0.3], [58.214, 22.897, -83.014, 0.3], [60.338, 26.929, -87.484, 0.3], [67.546, 26.644, -91.305, 0.3], [67.546, 26.644, -91.305, 0.3], [67.895, 26.63, -91.49, 0.3], [70.475, 29.987, -97.919, 0.3], [71.436, 32.595, -105.546, 0.3], [71.436, 32.595, -105.546, 0.3], [71.675, 33.244, -107.442, 0.3], [76.723, 30.573, -116.067, 0.3], [79.49, 29.691, -118.59, 0.3], [79.49, 29.691, -118.59, 0.3], [81.3, 29.115, -120.241, 0.3], [85.693, 33.478, -125.572, 0.3], [85.698, 37.657, -129.183, 0.3], [85.698, 37.657, -129.183, 0.3]])
        self._set_section_morphology(self.apic[129], [[0.0, 0.0, 0.0, 0.4], [3.087, -5.553, 1.767, 0.4], [2.71, -8.958, 4.359, 0.4], [2.71, -8.958, 4.359, 0.4], [2.64, -9.595, 4.844, 0.4], [2.912, -17.525, 10.068, 0.4], [2.94, -17.879, 10.534, 0.4], [2.94, -17.879, 10.534, 0.4], [3.252, -21.805, 15.708, 0.4], [5.224, -25.04, 17.922, 0.4]])
        self._set_section_morphology(self.apic[12], [[174.742, -42.389, -10.594, 1.6], [180.651, -43.727, -10.924, 1.6], [186.559, -45.066, -11.255, 1.6]])
        self._set_section_morphology(self.apic[130], [[5.224, -25.04, 17.922, 0.4], [4.475, -39.994, 21.246, 0.3], [4.31, -41.112, 21.355, 0.3], [4.31, -41.112, 21.355, 0.3], [3.117, -49.223, 22.151, 0.3], [1.923, -57.334, 22.947, 0.3], [1.923, -57.334, 22.947, 0.3], [1.821, -58.024, 23.015, 0.3], [-0.557, -73.52, 24.74, 0.3]])
        self._set_section_morphology(self.apic[131], [[-0.557, -73.52, 24.74, 0.3], [1.748, -85.772, 26.695, 0.3], [2.19, -88.509, 27.388, 0.3], [2.19, -88.509, 27.388, 0.3], [3.979, -99.568, 30.186, 0.3], [4.32, -103.199, 31.647, 0.3], [4.32, -103.199, 31.647, 0.3], [4.993, -110.357, 34.527, 0.3], [7.974, -115.483, 36.352, 0.3], [8.909, -116.681, 36.509, 0.3], [8.909, -116.681, 36.509, 0.3], [15.027, -124.516, 37.538, 0.3], [19.027, -128.265, 37.527, 0.3], [19.027, -128.265, 37.527, 0.3], [25.984, -134.784, 37.507, 0.3], [30.628, -138.403, 38.314, 0.3], [30.628, -138.403, 38.314, 0.3], [37.261, -143.573, 39.467, 0.3], [42.878, -147.613, 38.49, 0.3], [42.878, -147.613, 38.49, 0.3], [45.055, -149.179, 38.112, 0.3], [47.647, -153.15, 35.873, 0.3], [49.581, -157.435, 34.1, 0.3], [51.583, -158.071, 32.744, 0.3]])
        self._set_section_morphology(self.apic[132], [[-0.557, -73.52, 24.74, 0.3], [-6.404, -76.412, 20.416, 0.3], [-12.221, -83.506, 17.963, 0.3], [-12.221, -83.506, 17.963, 0.3], [-12.901, -84.335, 17.676, 0.3], [-19.423, -90.678, 14.896, 0.3], [-23.016, -96.241, 13.881, 0.3], [-23.016, -96.241, 13.881, 0.3], [-27.305, -102.881, 12.67, 0.3], [-30.656, -106.032, 9.018, 0.3], [-33.048, -108.064, 7.581, 0.3], [-33.048, -108.064, 7.581, 0.3], [-36.069, -110.63, 5.766, 0.3], [-39.518, -113.745, 3.61, 0.3], [-38.18, -118.874, 6.33, 0.3], [-38.014, -120.534, 7.203, 0.3], [-38.014, -120.534, 7.203, 0.3], [-37.367, -126.979, 10.591, 0.3], [-37.433, -136.914, 11.832, 0.3]])
        self._set_section_morphology(self.apic[133], [[5.224, -25.04, 17.922, 0.4], [1.698, -30.203, 22.327, 0.3], [1.001, -34.685, 26.902, 0.3], [0.628, -35.141, 27.094, 0.3], [0.628, -35.141, 27.094, 0.3], [-1.727, -38.014, 28.307, 0.3], [-0.739, -40.937, 30.95, 0.3], [-0.886, -46.543, 34.689, 0.3], [-0.886, -46.543, 34.689, 0.3], [-0.902, -47.161, 35.101, 0.3], [-4.658, -49.124, 34.902, 0.3], [-5.565, -56.164, 38.523, 0.3], [-5.878, -57.288, 39.834, 0.3], [-5.878, -57.288, 39.834, 0.3], [-6.769, -60.484, 43.561, 0.3], [-13.443, -64.134, 47.221, 0.3], [-14.48, -64.806, 47.551, 0.3], [-14.48, -64.806, 47.551, 0.3], [-18.883, -67.656, 48.954, 0.3], [-20.883, -73.306, 51.967, 0.3], [-21.16, -75.529, 53.233, 0.3], [-21.16, -75.529, 53.233, 0.3], [-21.448, -77.836, 54.547, 0.3], [-16.714, -84.039, 56.514, 0.3], [-13.718, -86.364, 57.762, 0.3], [-13.718, -86.364, 57.762, 0.3], [-12.18, -87.558, 58.402, 0.3], [-10.856, -92.149, 63.614, 0.3], [-5.779, -92.168, 65.953, 0.3]])
        self._set_section_morphology(self.apic[13], [[186.559, -45.066, -11.255, 1.6], [201.438, -49.758, -12.165, 1.6], [207.571, -52.219, -13.205, 1.6]])
        self._set_section_morphology(self.apic[14], [[207.571, -52.219, -13.205, 1.6], [224.215, -59.029, -11.442, 1.6], [238.403, -64.024, -11.389, 1.6]])
        self._set_section_morphology(self.apic[15], [[238.403, -64.024, -11.389, 1.6], [241.352, -65.744, -12.406, 1.6], [244.301, -67.463, -13.423, 1.6]])
        self._set_section_morphology(self.apic[16], [[244.301, -67.463, -13.423, 1.6], [251.161, -69.101, -13.683, 1.6], [258.021, -70.74, -13.943, 1.6]])
        self._set_section_morphology(self.apic[17], [[258.021, -70.74, -13.943, 1.6], [262.602, -72.971, -14.339, 1.6], [267.184, -75.203, -14.735, 1.6]])
        self._set_section_morphology(self.apic[18], [[267.184, -75.203, -14.735, 1.6], [269.699, -76.522, -15.289, 1.6], [272.215, -77.841, -15.843, 1.6]])
        self._set_section_morphology(self.apic[19], [[272.215, -77.841, -15.843, 1.6], [279.755, -81.529, -16.259, 1.6], [287.295, -85.217, -16.675, 1.6]])
        self._set_section_morphology(self.apic[1], [[39.121, -2.245, -2.457, 2.7], [48.494, -4.149, -2.295, 2.2], [55.455, -5.292, -1.809, 2.2]])
        self._set_section_morphology(self.apic[20], [[287.295, -85.217, -16.675, 1.6], [295.177, -89.537, -17.304, 1.6], [303.059, -93.858, -17.932, 1.6]])
        self._set_section_morphology(self.apic[21], [[303.059, -93.858, -17.932, 1.6], [305.261, -95.341, -18.503, 1.6], [307.464, -96.823, -19.074, 1.6]])
        self._set_section_morphology(self.apic[22], [[307.464, -96.823, -19.074, 1.6], [316.886, -101.888, -18.831, 1.6], [325.932, -106.84, -20.12, 1.6]])
        self._set_section_morphology(self.apic[23], [[325.932, -106.84, -20.12, 1.6], [331.867, -109.507, -22.922, 1.6], [337.802, -112.174, -25.724, 1.6]])
        self._set_section_morphology(self.apic[24], [[337.802, -112.174, -25.724, 1.6], [342.446, -113.377, -26.141, 1.6], [347.09, -114.579, -26.558, 1.6]])
        self._set_section_morphology(self.apic[25], [[347.09, -114.579, -26.558, 1.6], [357.78, -115.854, -27.326, 1.2], [361.619, -116.096, -27.717, 1.2], [361.619, -116.096, -27.717, 1.2], [368.897, -116.554, -28.456, 1.2], [376.175, -117.013, -29.196, 1.2], [376.175, -117.013, -29.196, 1.2], [378.543, -117.162, -29.436, 1.2], [387.363, -117.849, -30.844, 1.2], [390.584, -117.819, -31.635, 1.2]])
        self._set_section_morphology(self.apic[26], [[390.584, -117.819, -31.635, 1.2], [393.706, -117.751, -30.93, 1.2], [396.828, -117.684, -30.225, 1.2]])
        self._set_section_morphology(self.apic[27], [[396.828, -117.684, -30.225, 1.2], [409.013, -115.758, -30.472, 1.2], [429.354, -112.728, -29.709, 1.2]])
        self._set_section_morphology(self.apic[28], [[429.354, -112.728, -29.709, 1.2], [442.935, -107.565, -27.938, 1.2], [451.509, -105.019, -26.434, 1.2]])
        self._set_section_morphology(self.apic[29], [[451.509, -105.019, -26.434, 1.2], [455.004, -104.291, -27.976, 1.15], [458.499, -103.563, -29.518, 1.1]])
        self._set_section_morphology(self.apic[2], [[55.455, -5.292, -1.809, 2.2], [62.11, -6.868, -2.586, 2.2], [68.765, -8.444, -3.362, 2.2]])
        self._set_section_morphology(self.apic[30], [[458.499, -103.563, -29.518, 1.1], [464.708, -103.948, -29.851, 1.1], [470.918, -104.333, -30.185, 1.1]])
        self._set_section_morphology(self.apic[31], [[470.918, -104.333, -30.185, 1.1], [477.931, -108.133, -34.643, 0.8], [485.615, -112.66, -37.034, 0.8], [490.51, -116.312, -40.632, 0.8], [494.765, -119.754, -41.772, 0.8]])
        self._set_section_morphology(self.apic[32], [[494.765, -119.754, -41.772, 0.8], [497.156, -124.715, -45.503, 0.3], [500.457, -131.532, -48.127, 0.3], [502.465, -134.274, -51.436, 0.3]])
        self._set_section_morphology(self.apic[33], [[502.465, -134.274, -51.436, 0.3], [504.624, -142.824, -53.09, 0.3], [507.442, -147.397, -54.553, 0.3], [507.442, -147.397, -54.553, 0.3], [507.835, -148.035, -54.757, 0.3], [514.843, -149.729, -57.261, 0.3], [519.522, -150.001, -61.214, 0.3], [519.522, -150.001, -61.214, 0.3], [520.888, -150.08, -62.368, 0.3], [526.476, -149.755, -65.517, 0.3], [532.066, -148.653, -68.267, 0.3], [532.066, -148.653, -68.267, 0.3], [534.634, -148.147, -69.53, 0.3], [541.516, -145.612, -73.65, 0.3], [543.793, -144.547, -75.665, 0.3], [543.793, -144.547, -75.665, 0.3], [546.852, -143.117, -78.372, 0.3], [556.43, -143.526, -81.742, 0.3], [556.468, -143.524, -81.773, 0.3], [556.468, -143.524, -81.773, 0.3], [562.117, -143.238, -86.387, 0.3], [565.234, -144.235, -90.167, 0.3], [566.991, -144.574, -91.516, 0.3], [566.991, -144.574, -91.516, 0.3], [573.606, -145.848, -96.594, 0.3], [578.451, -146.34, -100.273, 0.3]])
        self._set_section_morphology(self.apic[34], [[578.451, -146.34, -100.273, 0.3], [580.432, -151.175, -105.037, 0.3], [582.671, -150.328, -110.423, 0.3], [584.827, -153.364, -112.733, 0.3], [584.827, -153.364, -112.733, 0.3], [586.522, -155.751, -114.549, 0.3], [590.061, -161.084, -121.203, 0.3], [590.15, -163.445, -125.232, 0.3], [590.15, -163.445, -125.232, 0.3], [590.323, -168.025, -133.045, 0.3], [591.081, -174.679, -137.93, 0.3], [591.081, -174.679, -137.93, 0.3], [591.441, -177.84, -140.251, 0.3], [591.099, -187.194, -147.062, 0.3], [590.96, -187.735, -148.808, 0.3], [590.96, -187.735, -148.808, 0.3], [590.345, -190.137, -156.563, 0.3], [588.343, -196.345, -163.059, 0.3]])
        self._set_section_morphology(self.apic[35], [[578.451, -146.34, -100.273, 0.3], [583.148, -143.634, -102.536, 0.3], [588.485, -147.424, -105.601, 0.3], [588.838, -146.564, -110.085, 0.3], [588.838, -146.564, -110.085, 0.3], [589.235, -145.598, -115.119, 0.3], [594.841, -151.592, -124.127, 0.3], [594.947, -151.587, -124.464, 0.3], [594.947, -151.587, -124.464, 0.3], [597.635, -151.457, -132.969, 0.3], [598.693, -148.495, -141.146, 0.3], [598.693, -148.495, -141.146, 0.3], [598.803, -148.188, -141.994, 0.3], [601.694, -151.764, -153.746, 0.3], [602.131, -151.917, -157.872, 0.3], [602.131, -151.917, -157.872, 0.3], [602.957, -152.206, -165.681, 0.3], [605.935, -151.606, -175.023, 0.3]])
        self._set_section_morphology(self.apic[36], [[502.465, -134.274, -51.436, 0.3], [506.905, -133.576, -51.662, 0.3], [513.31, -130.892, -55.817, 0.3], [516.284, -128.19, -57.589, 0.3], [516.284, -128.19, -57.589, 0.3], [518.015, -126.618, -58.619, 0.3], [522.744, -123.925, -61.381, 0.3], [528.149, -124.065, -64.03, 0.3], [529.721, -123.591, -65.647, 0.3], [529.721, -123.591, -65.647, 0.3], [533.218, -122.536, -69.247, 0.3], [540.75, -121.255, -73.293, 0.3], [543.671, -120.605, -74.455, 0.3], [543.671, -120.605, -74.455, 0.3], [549.502, -119.307, -76.775, 0.3], [559.615, -117.784, -79.154, 0.3], [559.688, -117.766, -79.165, 0.3], [559.688, -117.766, -79.165, 0.3], [568.861, -115.461, -80.607, 0.3], [575.451, -112.681, -82.566, 0.3], [575.451, -112.681, -82.566, 0.3], [578.806, -111.266, -83.563, 0.3], [586.215, -108.368, -86.154, 0.3], [589.738, -106.707, -89.031, 0.3], [589.738, -106.707, -89.031, 0.3], [594.846, -104.298, -93.203, 0.3], [602.831, -99.639, -96.916, 0.3], [602.831, -99.639, -96.916, 0.3], [603.58, -99.202, -97.264, 0.3], [613.158, -89.652, -100.877, 0.3], [614.512, -88.134, -101.123, 0.3], [614.512, -88.134, -101.123, 0.3], [622.28, -79.426, -102.531, 0.3], [626.677, -77.493, -104.602, 0.3], [626.677, -77.493, -104.602, 0.3], [629.904, -76.075, -106.121, 0.3], [636.546, -68.738, -107.868, 0.3], [638.199, -66.918, -109.749, 0.3], [638.199, -66.918, -109.749, 0.3], [642.082, -62.642, -114.168, 0.3], [646.987, -54.495, -116.138, 0.3], [646.987, -54.495, -116.138, 0.3], [650.3, -48.993, -117.469, 0.3], [654.984, -39.686, -117.801, 0.3], [654.984, -39.686, -117.801, 0.3], [655.993, -37.682, -117.872, 0.3], [658.953, -23.92, -113.502, 0.3]])
        self._set_section_morphology(self.apic[37], [[494.765, -119.754, -41.772, 0.8], [504.517, -118.097, -38.664, 0.3], [506.512, -116.99, -37.457, 0.3], [506.512, -116.99, -37.457, 0.3], [509.954, -115.08, -35.373, 0.3], [516.93, -111.037, -32.695, 0.3], [516.93, -111.037, -32.695, 0.3], [520.517, -108.958, -31.319, 0.3], [528.074, -105.285, -29.576, 0.3], [528.074, -105.285, -29.576, 0.3], [529.032, -104.819, -29.355, 0.3], [538.119, -98.255, -31.925, 0.3], [538.388, -98.1, -32.108, 0.3], [538.388, -98.1, -32.108, 0.3], [542.222, -95.889, -34.72, 0.3], [548.029, -91.437, -37.454, 0.3]])
        self._set_section_morphology(self.apic[38], [[548.029, -91.437, -37.454, 0.3], [552.591, -86.072, -40.793, 0.3], [557.68, -80.343, -42.603, 0.3], [558.633, -79.543, -42.757, 0.3], [558.633, -79.543, -42.757, 0.3], [564.941, -74.247, -43.778, 0.3], [569.378, -66.906, -44.648, 0.3], [569.378, -66.906, -44.648, 0.3], [569.464, -66.764, -44.665, 0.3], [577.62, -55.701, -43.897, 0.3], [579.711, -53.593, -43.559, 0.3], [579.711, -53.593, -43.559, 0.3], [585.943, -47.31, -42.552, 0.3], [591.508, -41.546, -42.326, 0.3], [591.508, -41.546, -42.326, 0.3], [592.153, -40.878, -42.3, 0.3], [595.457, -34.061, -43.753, 0.3], [598.469, -26.629, -45.741, 0.3], [598.48, -26.616, -45.742, 0.3], [598.48, -26.616, -45.742, 0.3], [603.61, -20.387, -46.056, 0.3], [607.637, -16.954, -50.386, 0.3], [609.004, -15.731, -51.206, 0.3], [609.004, -15.731, -51.206, 0.3], [611.532, -13.471, -52.721, 0.3], [615.067, -13.025, -56.008, 0.3], [621.44, -10.328, -59.664, 0.3], [621.854, -10.198, -59.974, 0.3], [621.854, -10.198, -59.974, 0.3], [626.41, -8.763, -63.385, 0.3], [636.249, -6.1, -64.306, 0.3], [636.974, -5.723, -64.309, 0.3], [636.974, -5.723, -64.309, 0.3], [645.047, -1.533, -64.34, 0.3], [651.439, 2.973, -64.029, 0.3], [651.439, 2.973, -64.029, 0.3], [653.786, 4.627, -63.915, 0.3], [661.231, 4.903, -63.933, 0.3], [665.876, 9.064, -66.085, 0.3], [665.876, 9.064, -66.085, 0.3], [668.147, 11.099, -67.138, 0.3], [673.469, 14.132, -69.368, 0.3], [679.834, 15.26, -72.485, 0.3], [679.834, 15.26, -72.485, 0.3]])
        self._set_section_morphology(self.apic[39], [[548.029, -91.437, -37.454, 0.3], [555.672, -87.561, -39.05, 0.3], [560.666, -83.567, -39.263, 0.3], [560.666, -83.567, -39.263, 0.3], [561.314, -83.049, -39.29, 0.3], [568.064, -80.465, -41.415, 0.3], [574.688, -79.22, -41.01, 0.3], [574.688, -79.22, -41.01, 0.3], [576.403, -78.897, -40.905, 0.3], [583.182, -76.831, -38.504, 0.3], [587.928, -73.606, -37.197, 0.3], [587.928, -73.606, -37.197, 0.3], [594.262, -69.302, -35.452, 0.3], [599.695, -66.036, -31.911, 0.3], [599.695, -66.036, -31.911, 0.3], [603.441, -63.784, -29.469, 0.3], [612.015, -58.716, -27.738, 0.3], [612.015, -58.716, -27.738, 0.3], [616.757, -55.913, -26.78, 0.3], [625.414, -52.402, -24.921, 0.3], [625.414, -52.402, -24.921, 0.3], [626.224, -52.073, -24.747, 0.3], [636.81, -51.205, -22.067, 0.3], [639.999, -51.137, -21.347, 0.3], [639.999, -51.137, -21.347, 0.3], [649.299, -50.936, -19.246, 0.3], [654.033, -51.401, -16.331, 0.3], [654.033, -51.401, -16.331, 0.3], [656.623, -51.655, -14.737, 0.3], [665.29, -53.324, -11.118, 0.3], [666.752, -51.908, -9.625, 0.3], [666.752, -51.908, -9.625, 0.3], [671.432, -47.373, -4.844, 0.3], [676.233, -42.498, -3.212, 0.3], [676.233, -42.498, -3.212, 0.3], [678.137, -40.565, -2.564, 0.3], [680.621, -36.613, 2.014, 0.3], [680.969, -39.325, 7.115, 0.3], [680.969, -39.325, 7.115, 0.3]])
        self._set_section_morphology(self.apic[3], [[68.765, -8.444, -3.362, 2.2], [81.441, -13.49, -4.409, 2.2], [89.57, -14.481, -4.853, 2.2]])
        self._set_section_morphology(self.apic[40], [[470.918, -104.333, -30.185, 1.1], [480.135, -94.649, -28.311, 0.4], [481.49, -93.02, -28.223, 0.4], [481.49, -93.02, -28.223, 0.4], [486.48, -87.02, -27.9, 0.4], [491.469, -81.021, -27.576, 0.4], [491.469, -81.021, -27.576, 0.4], [497.756, -73.461, -27.168, 0.4], [501.761, -69.347, -26.503, 0.4], [501.761, -69.347, -26.503, 0.4], [507.174, -63.788, -25.605, 0.4], [512.586, -58.23, -24.708, 0.4], [512.586, -58.23, -24.708, 0.4], [513.777, -57.006, -24.51, 0.4], [524.011, -47.646, -23.564, 0.4]])
        self._set_section_morphology(self.apic[41], [[524.011, -47.646, -23.564, 0.4], [529.55, -37.317, -18.94, 0.3], [531.843, -35.553, -18.38, 0.3], [531.843, -35.553, -18.38, 0.3], [539.711, -29.5, -16.458, 0.3], [543.752, -26.106, -15.16, 0.3], [543.752, -26.106, -15.16, 0.3], [554.248, -17.288, -11.789, 0.3], [555.306, -16.408, -11.403, 0.3], [555.306, -16.408, -11.403, 0.3], [565.236, -8.154, -7.78, 0.3], [566.907, -6.923, -7.281, 0.3], [566.907, -6.923, -7.281, 0.3], [572.991, -2.44, -5.462, 0.3], [579.075, 2.043, -3.642, 0.3], [579.075, 2.043, -3.642, 0.3], [579.205, 2.138, -3.604, 0.3], [587.286, 7.983, -2.713, 0.3], [590.377, 12.263, -1.749, 0.3], [590.377, 12.263, -1.749, 0.3], [596.237, 20.376, 0.079, 0.3], [598.397, 25.25, 0.746, 0.3], [598.397, 25.25, 0.746, 0.3], [602.967, 35.563, 2.156, 0.3], [605.819, 38.458, 3.126, 0.3], [605.819, 38.458, 3.126, 0.3], [609.672, 42.37, 4.436, 0.3], [616.015, 49.866, 5.708, 0.3], [616.015, 49.866, 5.708, 0.3], [621.937, 56.863, 6.895, 0.3], [625.882, 61.653, 7.998, 0.3], [625.882, 61.653, 7.998, 0.3], [626.053, 61.861, 8.046, 0.3], [637.539, 71.876, 9.059, 0.3], [637.539, 71.876, 9.059, 0.3]])
        self._set_section_morphology(self.apic[42], [[637.539, 71.876, 9.059, 0.3], [643.232, 77.588, 10.415, 0.3], [648.926, 83.301, 11.77, 0.3], [648.926, 83.301, 11.77, 0.3], [650.271, 84.65, 12.091, 0.3], [659.263, 88.64, 14.089, 0.3], [662.794, 91.199, 14.551, 0.3], [662.794, 91.199, 14.551, 0.3], [665.315, 93.026, 14.882, 0.3], [672.026, 97.728, 15.208, 0.3], [675.494, 100.793, 17.166, 0.3], [675.494, 100.793, 17.166, 0.3], [676.845, 101.986, 17.928, 0.3], [684.461, 106.938, 21.316, 0.3], [688.586, 106.452, 23.524, 0.3], [688.586, 106.452, 23.524, 0.3], [689.831, 106.305, 24.191, 0.3], [699.248, 113.306, 26.143, 0.3], [702.069, 112.419, 26.852, 0.3]])
        self._set_section_morphology(self.apic[43], [[637.539, 71.876, 9.059, 0.3], [649.054, 74.53, 6.745, 0.3], [651.308, 74.661, 6.89, 0.3], [651.308, 74.661, 6.89, 0.3], [664.504, 75.432, 7.739, 0.3], [665.541, 75.408, 7.953, 0.3], [665.541, 75.408, 7.953, 0.3], [675.298, 75.184, 9.96, 0.3], [679.555, 74.573, 9.379, 0.3], [679.555, 74.573, 9.379, 0.3], [687.482, 73.436, 8.298, 0.3], [691.386, 72.201, 7.082, 0.3], [693.318, 72.45, 7.203, 0.3], [693.318, 72.45, 7.203, 0.3], [698.472, 73.115, 7.526, 0.3], [707.431, 73.824, 8.941, 0.3], [707.431, 73.824, 8.941, 0.3], [709.124, 73.959, 9.209, 0.3], [713.971, 74.025, 15.04, 0.3], [717.928, 73.038, 17.936, 0.3], [717.928, 73.038, 17.936, 0.3], [722.324, 71.94, 21.154, 0.3], [730.523, 71.989, 24.199, 0.3]])
        self._set_section_morphology(self.apic[44], [[524.011, -47.646, -23.564, 0.4], [530.57, -47.095, -24.649, 0.3], [536.397, -47.232, -25.565, 0.3], [536.397, -47.232, -25.565, 0.3], [539.54, -47.306, -26.059, 0.3], [548.493, -50.126, -25.848, 0.3], [548.493, -50.126, -25.848, 0.3], [549.564, -50.464, -25.823, 0.3], [557.908, -51.001, -27.265, 0.3], [560.232, -51.046, -29.102, 0.3], [560.232, -51.046, -29.102, 0.3], [568.44, -51.205, -35.589, 0.3], [570.056, -51.571, -36.892, 0.3], [570.056, -51.571, -36.892, 0.3], [574.152, -52.498, -40.194, 0.3], [579.974, -54.869, -43.763, 0.3]])
        self._set_section_morphology(self.apic[45], [[579.974, -54.869, -43.763, 0.3], [579.646, -57.917, -45.214, 0.3], [577.0, -58.134, -45.884, 0.3]])
        self._set_section_morphology(self.apic[46], [[579.974, -54.869, -43.763, 0.3], [585.814, -56.716, -45.338, 0.3], [588.623, -60.234, -48.576, 0.3], [589.917, -63.266, -52.473, 0.3], [589.917, -63.266, -52.473, 0.3], [590.702, -65.106, -54.836, 0.3], [594.052, -68.798, -59.036, 0.3], [597.634, -68.902, -65.314, 0.3], [597.726, -68.866, -65.398, 0.3], [597.726, -68.866, -65.398, 0.3], [602.82, -66.883, -70.034, 0.3], [607.17, -67.751, -75.742, 0.3], [609.033, -67.984, -77.509, 0.3], [609.033, -67.984, -77.509, 0.3], [612.59, -68.429, -80.882, 0.3], [615.494, -69.373, -88.687, 0.3], [617.064, -68.899, -91.971, 0.3], [617.064, -68.899, -91.971, 0.3], [619.691, -68.107, -97.464, 0.3], [621.528, -65.566, -104.423, 0.3], [622.501, -64.835, -107.384, 0.3]])
        self._set_section_morphology(self.apic[47], [[458.499, -103.563, -29.518, 1.1], [461.919, -99.931, -31.888, 0.3], [467.08, -96.333, -36.648, 0.3], [468.678, -95.476, -38.16, 0.3], [468.678, -95.476, -38.16, 0.3], [472.6, -93.373, -41.87, 0.3], [475.604, -90.679, -49.758, 0.3], [475.991, -89.781, -50.304, 0.3], [475.991, -89.781, -50.304, 0.3], [478.78, -83.309, -54.24, 0.3], [482.783, -79.374, -59.513, 0.3], [482.783, -79.374, -59.513, 0.3], [483.206, -78.958, -60.07, 0.3], [489.351, -75.671, -65.259, 0.3], [492.729, -71.647, -68.682, 0.3], [492.729, -71.647, -68.682, 0.3], [493.17, -71.122, -69.129, 0.3], [499.233, -64.662, -73.9, 0.3], [502.653, -61.467, -75.326, 0.3], [502.653, -61.467, -75.326, 0.3], [510.129, -54.482, -78.444, 0.3], [513.925, -51.261, -79.447, 0.3], [513.925, -51.261, -79.447, 0.3], [518.231, -47.607, -80.584, 0.3], [521.203, -38.057, -80.121, 0.3]])
        self._set_section_morphology(self.apic[48], [[451.509, -105.019, -26.434, 1.2], [457.489, -98.502, -22.691, 0.3], [459.07, -96.318, -19.661, 0.3], [459.07, -96.318, -19.661, 0.3], [461.212, -93.357, -15.554, 0.3], [463.764, -88.563, -9.46, 0.3], [463.764, -88.563, -9.46, 0.3], [464.81, -86.596, -6.961, 0.3], [467.529, -81.666, -1.389, 0.3], [469.246, -81.233, 0.218, 0.3], [469.246, -81.233, 0.218, 0.3], [474.965, -79.789, 5.57, 0.3], [477.805, -77.854, 10.112, 0.3], [477.805, -77.854, 10.112, 0.3], [480.785, -75.822, 14.879, 0.3], [484.227, -72.662, 20.977, 0.3], [484.227, -72.662, 20.977, 0.3], [488.906, -68.368, 29.266, 0.3], [490.56, -66.576, 31.366, 0.3], [490.56, -66.576, 31.366, 0.3], [493.795, -63.07, 35.473, 0.3], [497.857, -59.091, 40.154, 0.3]])
        self._set_section_morphology(self.apic[49], [[497.857, -59.091, 40.154, 0.3], [496.721, -56.086, 47.023, 0.3], [498.683, -54.637, 51.043, 0.3], [498.683, -54.637, 51.043, 0.3], [500.729, -53.125, 55.234, 0.3], [502.863, -57.234, 60.985, 0.3], [502.863, -57.234, 60.985, 0.3], [503.641, -58.732, 63.082, 0.3], [506.446, -61.779, 71.736, 0.3], [506.446, -61.779, 71.736, 0.3], [506.991, -62.371, 73.415, 0.3], [508.145, -64.796, 83.074, 0.3], [508.233, -64.883, 83.453, 0.3], [508.233, -64.883, 83.453, 0.3], [510.4, -67.043, 92.801, 0.3], [510.92, -68.248, 94.869, 0.3]])
        self._set_section_morphology(self.apic[4], [[89.57, -14.481, -4.853, 2.2], [103.974, -19.023, -5.799, 2.2], [112.245, -21.105, -5.704, 2.2]])
        self._set_section_morphology(self.apic[50], [[497.857, -59.091, 40.154, 0.3], [505.094, -47.74, 40.353, 0.3], [507.438, -44.807, 41.037, 0.3], [507.438, -44.807, 41.037, 0.3], [516.817, -33.073, 43.774, 0.3], [518.033, -31.54, 43.316, 0.3], [518.033, -31.54, 43.316, 0.3], [520.472, -28.463, 42.398, 0.3], [530.047, -19.418, 43.81, 0.3]])
        self._set_section_morphology(self.apic[51], [[530.047, -19.418, 43.81, 0.3], [539.399, -12.393, 46.76, 0.3], [543.314, -9.901, 48.143, 0.3], [543.314, -9.901, 48.143, 0.3], [547.673, -7.126, 49.682, 0.3], [551.35, -4.602, 53.371, 0.3], [554.51, -0.071, 54.876, 0.3], [554.51, -0.071, 54.876, 0.3], [555.851, 1.852, 55.515, 0.3], [562.365, 6.626, 58.835, 0.3], [566.845, 9.514, 60.974, 0.3], [566.845, 9.514, 60.974, 0.3], [570.574, 11.917, 62.754, 0.3], [576.889, 13.091, 67.652, 0.3], [580.025, 13.206, 70.208, 0.3], [580.025, 13.206, 70.208, 0.3], [582.904, 13.311, 72.554, 0.3], [587.324, 16.652, 76.773, 0.3], [590.804, 21.33, 78.956, 0.3], [590.804, 21.33, 78.956, 0.3], [592.386, 23.456, 79.948, 0.3], [597.274, 25.079, 84.741, 0.3], [603.683, 27.409, 86.49, 0.3], [603.683, 27.409, 86.49, 0.3], [611.2, 30.141, 88.541, 0.3], [619.488, 32.561, 89.028, 0.3], [619.488, 32.561, 89.028, 0.3], [625.022, 34.176, 89.353, 0.3], [634.815, 37.389, 91.422, 0.3], [635.434, 37.399, 91.414, 0.3], [635.434, 37.399, 91.414, 0.3], [641.158, 37.487, 91.336, 0.3], [651.752, 40.947, 90.448, 0.3], [651.752, 40.947, 90.448, 0.3], [651.773, 40.954, 90.447, 0.3], [658.665, 42.446, 88.859, 0.3], [667.987, 44.364, 87.238, 0.3], [667.987, 44.364, 87.238, 0.3], [675.755, 45.962, 85.888, 0.3], [683.022, 49.952, 82.76, 0.3], [683.022, 49.952, 82.76, 0.3]])
        self._set_section_morphology(self.apic[52], [[530.047, -19.418, 43.81, 0.3], [534.301, -12.846, 44.511, 0.3], [538.554, -6.274, 45.213, 0.3], [538.554, -6.274, 45.213, 0.3], [541.042, -2.431, 45.623, 0.3], [547.534, 6.525, 46.787, 0.3], [547.534, 6.525, 46.787, 0.3], [554.659, 16.354, 48.065, 0.3], [556.702, 19.2, 48.315, 0.3], [556.702, 19.2, 48.315, 0.3], [565.712, 31.749, 49.419, 0.3], [565.867, 31.908, 49.482, 0.3], [565.867, 31.908, 49.482, 0.3], [573.904, 40.189, 52.76, 0.3], [576.511, 42.766, 53.409, 0.3], [576.511, 42.766, 53.409, 0.3], [583.564, 49.736, 55.167, 0.3], [586.614, 54.231, 56.717, 0.3], [586.614, 54.231, 56.717, 0.3], [590.897, 60.545, 58.895, 0.3], [595.918, 66.396, 59.97, 0.3], [595.918, 66.396, 59.97, 0.3], [602.235, 73.757, 61.323, 0.3], [606.464, 77.677, 62.686, 0.3], [606.464, 77.677, 62.686, 0.3], [609.416, 80.414, 63.638, 0.3], [612.333, 88.946, 67.632, 0.3], [612.674, 90.427, 68.439, 0.3], [612.674, 90.427, 68.439, 0.3], [615.037, 100.699, 74.038, 0.3], [616.001, 104.084, 75.428, 0.3], [616.001, 104.084, 75.428, 0.3], [617.78, 110.334, 77.993, 0.3], [621.674, 116.986, 82.097, 0.3], [621.674, 116.986, 82.097, 0.3]])
        self._set_section_morphology(self.apic[53], [[429.354, -112.728, -29.709, 1.2], [433.482, -121.902, -32.22, 0.3], [436.561, -126.625, -32.978, 0.3], [436.561, -126.625, -32.978, 0.3], [442.091, -135.108, -34.338, 0.3], [446.253, -138.565, -36.535, 0.3], [446.253, -138.565, -36.535, 0.3], [450.257, -141.89, -38.647, 0.3], [454.956, -148.92, -44.77, 0.3], [454.956, -148.92, -44.77, 0.3], [455.607, -149.893, -45.618, 0.3], [458.521, -161.839, -50.648, 0.3], [458.786, -163.058, -51.098, 0.3], [458.786, -163.058, -51.098, 0.3], [461.461, -175.365, -55.638, 0.3], [461.814, -177.951, -56.196, 0.3], [461.814, -177.951, -56.196, 0.3], [463.109, -187.427, -58.242, 0.3], [464.984, -193.333, -59.244, 0.3], [464.984, -193.333, -59.244, 0.3], [466.07, -196.754, -59.825, 0.3], [470.074, -204.31, -60.88, 0.3], [472.377, -207.26, -61.567, 0.3], [472.377, -207.26, -61.567, 0.3], [477.682, -214.055, -63.149, 0.3], [481.967, -219.681, -64.927, 0.3], [481.967, -219.681, -64.927, 0.3], [484.522, -223.036, -65.988, 0.3], [489.702, -228.872, -68.511, 0.3], [492.535, -230.915, -68.824, 0.3], [492.535, -230.915, -68.824, 0.3], [497.462, -234.466, -69.368, 0.3], [502.295, -242.671, -72.284, 0.3], [502.295, -242.671, -72.284, 0.3], [502.399, -242.847, -72.347, 0.3], [504.539, -251.923, -75.994, 0.3], [505.891, -257.59, -75.767, 0.3], [505.891, -257.59, -75.767, 0.3]])
        self._set_section_morphology(self.apic[54], [[396.828, -117.684, -30.225, 1.2], [405.921, -129.471, -32.847, 0.3], [408.019, -131.464, -33.699, 0.3], [408.019, -131.464, -33.699, 0.3], [415.031, -138.122, -36.547, 0.3], [421.483, -141.187, -40.266, 0.3], [421.483, -141.187, -40.266, 0.3], [424.997, -142.856, -42.292, 0.3], [430.825, -147.334, -47.813, 0.3], [432.721, -149.359, -51.425, 0.3], [432.721, -149.359, -51.425, 0.3], [434.339, -151.087, -54.508, 0.3], [438.764, -156.696, -60.094, 0.3], [440.252, -160.589, -63.164, 0.3], [440.252, -160.589, -63.164, 0.3], [441.278, -163.274, -65.282, 0.3], [444.035, -167.306, -70.014, 0.3], [449.439, -171.12, -74.076, 0.3]])
        self._set_section_morphology(self.apic[55], [[390.584, -117.819, -31.635, 1.2], [395.92, -115.324, -36.357, 0.3], [399.833, -110.601, -40.292, 0.3], [399.833, -110.601, -40.292, 0.3], [400.731, -109.518, -41.195, 0.3], [405.848, -104.865, -47.989, 0.3], [408.534, -104.729, -50.182, 0.3], [408.534, -104.729, -50.182, 0.3], [411.535, -104.577, -52.634, 0.3], [416.159, -106.585, -59.799, 0.3], [417.632, -106.603, -61.429, 0.3], [417.632, -106.603, -61.429, 0.3], [421.286, -106.648, -65.474, 0.3], [426.58, -109.384, -70.573, 0.3], [427.938, -109.668, -71.248, 0.3], [427.938, -109.668, -71.248, 0.3], [436.281, -111.41, -75.398, 0.3], [440.658, -111.516, -78.484, 0.3], [440.658, -111.516, -78.484, 0.3], [443.428, -111.583, -80.437, 0.3], [449.191, -112.363, -83.547, 0.3], [451.869, -114.822, -86.761, 0.3], [451.869, -114.822, -86.761, 0.3], [452.692, -115.578, -87.749, 0.3], [454.738, -120.438, -93.511, 0.3], [458.041, -121.01, -97.915, 0.3], [458.041, -121.01, -97.915, 0.3], [461.88, -121.675, -103.035, 0.3], [467.538, -122.568, -109.183, 0.3], [467.538, -122.568, -109.183, 0.3], [468.382, -122.701, -110.1, 0.3], [477.444, -127.686, -118.905, 0.3], [477.444, -127.686, -118.905, 0.3]])
        self._set_section_morphology(self.apic[56], [[347.09, -114.579, -26.558, 1.6], [350.875, -119.978, -29.685, 0.3], [353.501, -123.961, -32.422, 0.3]])
        self._set_section_morphology(self.apic[57], [[353.501, -123.961, -32.422, 0.3], [352.648, -126.867, -40.427, 0.3], [354.184, -131.308, -46.8, 0.3], [354.184, -131.308, -46.8, 0.3], [354.285, -131.601, -47.221, 0.3], [354.808, -135.471, -56.616, 0.3], [353.222, -138.214, -61.449, 0.3], [353.222, -138.214, -61.449, 0.3], [352.488, -139.484, -63.687, 0.3], [353.055, -144.408, -71.048, 0.3], [356.922, -145.417, -73.927, 0.3], [356.922, -145.417, -73.927, 0.3], [362.262, -146.81, -77.902, 0.3], [367.76, -152.121, -83.834, 0.3], [367.76, -152.121, -83.834, 0.3], [369.555, -153.855, -85.771, 0.3], [371.571, -155.029, -89.619, 0.3], [374.339, -150.143, -92.063, 0.3], [373.97, -148.462, -94.133, 0.3]])
        self._set_section_morphology(self.apic[58], [[353.501, -123.961, -32.422, 0.3], [360.3, -134.497, -34.224, 0.3], [361.706, -137.679, -34.299, 0.3], [361.706, -137.679, -34.299, 0.3], [364.968, -145.062, -34.473, 0.3], [368.229, -152.445, -34.648, 0.3], [368.229, -152.445, -34.648, 0.3], [368.911, -153.988, -34.685, 0.3], [376.856, -165.403, -34.384, 0.3], [377.152, -165.865, -34.353, 0.3], [377.152, -165.865, -34.353, 0.3], [381.062, -171.969, -33.947, 0.3], [383.453, -180.528, -33.953, 0.3], [383.453, -180.528, -33.953, 0.3], [384.274, -183.466, -33.956, 0.3], [392.689, -192.924, -31.667, 0.3], [392.831, -193.107, -31.653, 0.3], [392.831, -193.107, -31.653, 0.3], [397.521, -199.163, -31.197, 0.3], [399.033, -207.462, -30.395, 0.3], [399.033, -207.462, -30.395, 0.3], [399.04, -207.502, -30.392, 0.3], [398.345, -215.154, -32.256, 0.3], [399.949, -222.992, -30.455, 0.3]])
        self._set_section_morphology(self.apic[59], [[337.802, -112.174, -25.724, 1.6], [342.429, -116.792, -29.818, 0.3], [344.882, -123.876, -34.112, 0.3], [344.882, -123.876, -34.112, 0.3], [345.085, -124.462, -34.468, 0.3], [352.295, -136.199, -41.87, 0.3], [352.295, -136.199, -41.87, 0.3], [353.496, -138.153, -43.103, 0.3], [360.495, -149.084, -47.635, 0.3], [360.495, -149.084, -47.635, 0.3], [361.501, -150.655, -48.286, 0.3], [367.064, -158.71, -51.231, 0.3], [368.369, -162.511, -52.286, 0.3], [368.369, -162.511, -52.286, 0.3], [371.307, -171.068, -54.66, 0.3], [374.093, -177.26, -56.355, 0.3], [374.093, -177.26, -56.355, 0.3], [375.435, -180.242, -57.172, 0.3], [379.303, -188.813, -60.717, 0.3], [380.009, -191.533, -61.558, 0.3], [380.009, -191.533, -61.558, 0.3], [381.528, -197.388, -63.369, 0.3], [381.549, -206.317, -66.157, 0.3], [381.256, -206.875, -66.424, 0.3], [381.256, -206.875, -66.424, 0.3], [377.054, -214.876, -70.254, 0.3], [374.995, -219.781, -74.053, 0.3], [374.995, -219.781, -74.053, 0.3], [372.963, -224.624, -77.803, 0.3], [371.319, -231.47, -84.761, 0.3], [371.319, -231.47, -84.761, 0.3]])
        self._set_section_morphology(self.apic[5], [[112.245, -21.105, -5.704, 2.2], [122.876, -24.461, -7.429, 2.2], [126.356, -25.032, -7.186, 2.2]])
        self._set_section_morphology(self.apic[60], [[325.932, -106.84, -20.12, 1.6], [334.179, -113.627, -18.409, 0.3], [338.458, -116.453, -17.027, 0.3], [338.458, -116.453, -17.027, 0.3], [350.818, -124.616, -13.035, 0.3], [351.538, -124.889, -12.869, 0.3], [351.538, -124.889, -12.869, 0.3], [358.91, -127.684, -11.174, 0.3], [366.282, -130.478, -9.479, 0.3], [366.282, -130.478, -9.479, 0.3], [367.004, -130.752, -9.313, 0.3], [381.226, -135.706, -6.407, 0.3], [381.226, -135.706, -6.407, 0.3], [382.423, -136.123, -6.162, 0.3], [397.052, -137.581, -4.162, 0.3], [397.052, -137.581, -4.162, 0.3], [397.056, -137.581, -4.161, 0.3], [408.493, -140.65, -1.328, 0.3], [411.889, -141.028, 0.65, 0.3], [411.889, -141.028, 0.65, 0.3], [416.293, -141.519, 3.216, 0.3], [426.839, -143.475, 5.689, 0.3], [426.839, -143.475, 5.689, 0.3], [428.506, -143.784, 6.08, 0.3], [438.175, -148.914, 9.849, 0.3], [440.147, -149.899, 11.595, 0.3], [440.147, -149.899, 11.595, 0.3], [443.763, -151.705, 14.797, 0.3], [450.748, -151.259, 21.761, 0.3], [451.703, -151.377, 22.29, 0.3], [451.703, -151.377, 22.29, 0.3], [459.024, -152.277, 26.341, 0.3], [461.395, -155.395, 32.985, 0.3], [461.395, -155.395, 32.985, 0.3], [461.619, -155.689, 33.612, 0.3], [467.911, -159.221, 40.127, 0.3], [470.886, -162.241, 43.906, 0.3], [470.886, -162.241, 43.906, 0.3]])
        self._set_section_morphology(self.apic[61], [[307.464, -96.823, -19.074, 1.6], [314.459, -91.188, -25.768, 0.3], [317.586, -89.109, -27.194, 0.3], [317.586, -89.109, -27.194, 0.3], [321.4, -86.572, -28.933, 0.3], [328.322, -82.481, -34.09, 0.3], [328.685, -82.256, -34.727, 0.3], [328.685, -82.256, -34.727, 0.3], [332.212, -80.063, -40.911, 0.3], [330.771, -75.96, -46.619, 0.3], [330.953, -75.716, -47.129, 0.3], [330.953, -75.716, -47.129, 0.3], [333.6, -72.162, -54.546, 0.3], [330.551, -74.361, -59.946, 0.3], [330.551, -74.361, -59.946, 0.3], [329.527, -75.1, -61.759, 0.3], [324.614, -75.142, -66.592, 0.3], [321.78, -76.887, -71.248, 0.3], [321.686, -76.883, -71.632, 0.3], [321.686, -76.883, -71.632, 0.3], [319.776, -76.81, -79.401, 0.3], [319.501, -79.267, -86.183, 0.3], [319.501, -79.267, -86.183, 0.3], [319.433, -79.878, -87.87, 0.3], [323.384, -81.663, -92.077, 0.3], [325.105, -85.896, -97.875, 0.3]])
        self._set_section_morphology(self.apic[62], [[303.059, -93.858, -17.932, 1.6], [315.002, -100.764, -16.978, 0.3], [317.971, -103.418, -15.894, 0.3], [317.971, -103.418, -15.894, 0.3], [322.232, -107.226, -14.339, 0.3], [329.752, -116.092, -11.234, 0.3], [329.752, -116.092, -11.234, 0.3], [330.106, -116.51, -11.088, 0.3], [342.602, -124.632, -8.563, 0.3], [344.375, -125.407, -7.371, 0.3], [344.375, -125.407, -7.371, 0.3], [351.012, -128.31, -2.907, 0.3], [359.56, -131.585, -0.574, 0.3], [359.56, -131.585, -0.574, 0.3], [366.215, -134.134, 1.243, 0.3], [375.877, -137.762, 3.666, 0.3], [375.877, -137.762, 3.666, 0.3], [383.32, -140.556, 5.533, 0.3], [392.601, -141.826, 8.376, 0.3], [392.601, -141.826, 8.376, 0.3], [398.114, -142.58, 10.065, 0.3], [409.19, -145.583, 14.029, 0.3], [409.19, -145.583, 14.029, 0.3], [410.404, -145.912, 14.464, 0.3], [423.052, -149.884, 18.401, 0.3], [425.318, -150.04, 20.032, 0.3], [425.318, -150.04, 20.032, 0.3], [433.811, -150.624, 26.145, 0.3], [439.776, -149.376, 30.473, 0.3], [439.776, -149.376, 30.473, 0.3], [442.857, -148.732, 32.708, 0.3], [448.03, -149.292, 38.576, 0.3], [453.912, -149.327, 40.695, 0.3], [453.912, -149.327, 40.695, 0.3], [458.249, -149.353, 42.258, 0.3], [466.834, -147.849, 46.295, 0.3], [469.857, -147.746, 48.496, 0.3], [469.857, -147.746, 48.496, 0.3]])
        self._set_section_morphology(self.apic[63], [[287.295, -85.217, -16.675, 1.6], [298.402, -78.763, -18.608, 0.3], [301.999, -77.15, -18.994, 0.3], [301.999, -77.15, -18.994, 0.3], [310.753, -73.224, -19.935, 0.3], [317.888, -71.648, -19.696, 0.3], [317.888, -71.648, -19.696, 0.3], [329.341, -69.118, -19.313, 0.3], [334.374, -68.082, -19.007, 0.3], [334.436, -68.053, -18.998, 0.3], [334.436, -68.053, -18.998, 0.3], [345.902, -62.796, -17.375, 0.3], [350.103, -62.434, -17.752, 0.3], [350.103, -62.434, -17.752, 0.3], [352.428, -62.234, -17.961, 0.3], [367.027, -62.132, -17.452, 0.3], [367.027, -62.132, -17.452, 0.3], [368.712, -62.12, -17.393, 0.3], [381.619, -60.408, -14.08, 0.3], [383.418, -60.092, -13.969, 0.3], [383.418, -60.092, -13.969, 0.3], [396.568, -57.776, -13.16, 0.3], [400.118, -57.521, -12.831, 0.3], [400.118, -57.521, -12.831, 0.3], [414.189, -56.507, -11.53, 0.3], [416.946, -56.873, -11.66, 0.3], [416.946, -56.873, -11.66, 0.3], [422.793, -57.647, -11.938, 0.3], [426.848, -58.405, -13.156, 0.3], [432.648, -61.808, -13.694, 0.3], [432.648, -61.808, -13.694, 0.3]])
        self._set_section_morphology(self.apic[64], [[272.215, -77.841, -15.843, 1.6], [285.748, -72.686, -20.591, 0.3], [288.242, -71.961, -20.517, 0.3], [288.242, -71.961, -20.517, 0.3], [303.058, -67.654, -20.076, 0.3], [305.43, -67.281, -20.176, 0.3], [305.43, -67.281, -20.176, 0.3], [317.48, -65.385, -20.686, 0.3], [322.961, -65.397, -21.97, 0.3], [322.961, -65.397, -21.97, 0.3], [330.839, -65.412, -23.816, 0.3], [340.355, -65.562, -25.917, 0.3], [340.355, -65.562, -25.917, 0.3], [343.063, -65.605, -26.515, 0.3], [355.697, -65.922, -28.182, 0.3], [358.005, -65.819, -28.373, 0.3], [358.005, -65.819, -28.373, 0.3], [365.887, -65.466, -29.026, 0.3], [375.663, -65.721, -30.697, 0.3], [375.663, -65.721, -30.697, 0.3], [378.553, -65.796, -31.191, 0.3], [392.322, -65.949, -33.289, 0.3], [393.276, -66.103, -33.433, 0.3], [393.276, -66.103, -33.433, 0.3], [405.966, -68.158, -35.344, 0.3], [410.555, -69.426, -36.229, 0.3], [410.555, -69.426, -36.229, 0.3], [419.191, -71.811, -37.893, 0.3], [427.896, -72.347, -38.152, 0.3], [427.896, -72.347, -38.152, 0.3], [429.523, -72.447, -38.2, 0.3], [441.683, -78.9, -38.244, 0.3], [444.011, -79.633, -38.202, 0.3], [444.011, -79.633, -38.202, 0.3], [450.755, -81.758, -38.079, 0.3], [455.761, -82.815, -39.227, 0.3], [460.718, -80.712, -40.456, 0.3], [460.718, -80.712, -40.456, 0.3]])
        self._set_section_morphology(self.apic[65], [[267.184, -75.203, -14.735, 1.6], [270.762, -69.485, -15.574, 1.04], [274.34, -63.767, -16.414, 0.48], [274.34, -63.767, -16.414, 0.48], [274.853, -62.947, -16.534, 0.4], [280.467, -54.244, -19.886, 0.4], [281.851, -53.199, -19.82, 0.4], [281.851, -53.199, -19.82, 0.4], [287.328, -49.065, -19.561, 0.4], [293.113, -45.645, -19.264, 0.4]])
        self._set_section_morphology(self.apic[66], [[293.113, -45.645, -19.264, 0.4], [308.279, -48.845, -17.686, 0.4], [308.798, -48.804, -17.792, 0.4], [308.798, -48.804, -17.792, 0.4], [317.583, -48.114, -19.597, 0.4], [324.543, -48.823, -20.901, 0.4], [324.543, -48.823, -20.901, 0.4], [327.387, -49.113, -21.434, 0.4], [335.147, -48.422, -23.947, 0.4], [339.7, -47.769, -25.953, 0.4], [339.7, -47.769, -25.953, 0.4], [343.122, -47.278, -27.46, 0.4], [350.118, -47.929, -32.497, 0.4], [353.522, -47.964, -33.933, 0.4], [353.522, -47.964, -33.933, 0.4], [360.388, -48.035, -36.831, 0.4], [365.361, -49.081, -37.48, 0.4], [368.724, -50.141, -37.734, 0.4]])
        self._set_section_morphology(self.apic[67], [[293.113, -45.645, -19.264, 0.4], [299.872, -37.819, -20.513, 0.4], [306.605, -34.545, -20.437, 0.4], [306.605, -34.545, -20.437, 0.4], [311.649, -32.093, -20.379, 0.4], [322.645, -26.6, -20.085, 0.4], [322.645, -26.6, -20.085, 0.4], [330.313, -22.769, -19.88, 0.4], [338.345, -18.034, -20.198, 0.4], [338.345, -18.034, -20.198, 0.4], [341.321, -16.279, -20.316, 0.4], [351.996, -10.73, -20.25, 0.4], [353.578, -8.906, -20.191, 0.4], [353.578, -8.906, -20.191, 0.4], [360.21, -1.26, -19.941, 0.4], [362.809, 5.792, -17.937, 0.4]])
        self._set_section_morphology(self.apic[68], [[258.021, -70.74, -13.943, 1.6], [269.05, -70.009, -10.729, 0.4], [275.075, -69.854, -8.381, 0.4], [275.075, -69.854, -8.381, 0.4], [282.952, -69.652, -5.311, 0.4], [291.663, -71.25, -1.808, 0.4], [291.663, -71.25, -1.808, 0.4], [295.034, -71.868, -0.452, 0.4], [308.04, -70.728, 5.365, 0.4], [308.04, -70.728, 5.365, 0.4], [308.102, -70.722, 5.392, 0.4], [319.959, -68.674, 10.133, 0.4], [324.732, -69.404, 11.348, 0.4], [324.732, -69.404, 11.348, 0.4], [336.214, -71.16, 14.271, 0.4], [342.125, -71.758, 15.126, 0.4], [342.125, -71.758, 15.126, 0.4], [355.872, -73.15, 17.117, 0.4], [359.676, -73.59, 18.34, 0.4], [359.676, -73.59, 18.34, 0.4], [371.735, -74.984, 22.216, 0.4], [376.656, -75.775, 23.82, 0.4], [376.656, -75.775, 23.82, 0.4], [385.427, -77.185, 26.679, 0.4], [393.145, -79.606, 29.738, 0.4], [393.145, -79.606, 29.738, 0.4], [399.404, -81.569, 32.218, 0.4], [409.485, -84.162, 35.672, 0.4], [409.485, -84.162, 35.672, 0.4], [417.931, -86.335, 38.566, 0.4], [426.395, -87.372, 40.7, 0.4], [426.395, -87.372, 40.7, 0.4], [434.335, -88.344, 42.702, 0.4], [443.022, -92.657, 41.876, 0.4], [443.022, -92.657, 41.876, 0.4]])
        self._set_section_morphology(self.apic[69], [[244.301, -67.463, -13.423, 1.6], [247.77, -76.951, -15.469, 0.4], [253.666, -84.064, -18.917, 0.4]])
        self._set_section_morphology(self.apic[6], [[126.356, -25.032, -7.186, 2.2], [128.871, -26.351, -7.74, 2.2], [131.387, -27.67, -8.294, 2.2]])
        self._set_section_morphology(self.apic[70], [[253.666, -84.064, -18.917, 0.4], [268.754, -89.872, -20.288, 0.4], [272.116, -91.034, -20.038, 0.4], [272.116, -91.034, -20.038, 0.4], [285.731, -95.741, -19.027, 0.4], [290.695, -97.735, -19.062, 0.4], [290.695, -97.735, -19.062, 0.4], [303.933, -103.05, -19.154, 0.4], [308.954, -105.122, -20.166, 0.4], [308.954, -105.122, -20.166, 0.4], [314.772, -107.522, -21.339, 0.4], [323.297, -111.269, -24.696, 0.4], [326.694, -111.838, -25.261, 0.4], [326.694, -111.838, -25.261, 0.4], [333.903, -113.045, -26.461, 0.4], [341.313, -116.432, -27.394, 0.4], [343.553, -118.7, -24.685, 0.4]])
        self._set_section_morphology(self.apic[71], [[253.666, -84.064, -18.917, 0.4], [253.985, -89.429, -24.779, 0.4], [255.906, -96.346, -30.499, 0.4], [256.704, -97.057, -32.02, 0.4], [256.704, -97.057, -32.02, 0.4], [258.671, -98.81, -35.77, 0.4], [257.263, -101.004, -40.32, 0.4], [254.703, -102.838, -48.926, 0.4], [254.703, -102.838, -48.926, 0.4], [254.691, -102.847, -48.966, 0.4], [252.475, -105.833, -53.048, 0.4], [253.958, -111.549, -54.816, 0.4], [258.929, -116.269, -56.88, 0.4], [259.001, -116.33, -56.922, 0.4], [259.001, -116.33, -56.922, 0.4], [261.94, -118.797, -58.625, 0.4], [272.645, -120.609, -61.886, 0.4], [275.782, -122.016, -62.243, 0.4], [275.782, -122.016, -62.243, 0.4], [280.53, -124.145, -62.784, 0.4], [286.494, -127.609, -65.815, 0.4], [291.757, -126.658, -69.001, 0.4]])
        self._set_section_morphology(self.apic[72], [[238.403, -64.024, -11.389, 1.6], [249.33, -60.646, -9.75, 0.4], [255.56, -60.839, -7.277, 0.4], [255.56, -60.839, -7.277, 0.4], [266.021, -61.163, -3.125, 0.4], [272.033, -61.887, 0.388, 0.4], [272.033, -61.887, 0.388, 0.4], [279.634, -62.802, 4.829, 0.4], [286.108, -66.615, 10.493, 0.4], [286.108, -66.615, 10.493, 0.4], [287.202, -67.26, 11.45, 0.4], [295.982, -72.619, 19.177, 0.4], [298.734, -74.986, 20.314, 0.4], [298.734, -74.986, 20.314, 0.4], [303.655, -79.219, 22.349, 0.4], [312.953, -83.634, 27.383, 0.4], [312.953, -83.634, 27.383, 0.4], [313.376, -83.835, 27.613, 0.4], [326.201, -85.236, 33.002, 0.4], [329.642, -84.762, 34.432, 0.4], [329.642, -84.762, 34.432, 0.4], [338.977, -83.475, 38.311, 0.4], [346.574, -82.023, 40.611, 0.4], [346.574, -82.023, 40.611, 0.4], [349.354, -81.491, 41.452, 0.4], [360.258, -82.818, 44.708, 0.4], [363.918, -82.687, 45.898, 0.4], [363.918, -82.687, 45.898, 0.4], [373.75, -82.335, 49.093, 0.4], [380.97, -81.939, 52.314, 0.4], [380.97, -81.939, 52.314, 0.4], [390.826, -81.397, 56.71, 0.4], [397.911, -81.144, 59.013, 0.4], [397.911, -81.144, 59.013, 0.4], [404.319, -80.914, 61.095, 0.4], [414.778, -78.43, 65.231, 0.4], [414.778, -78.43, 65.231, 0.4], [414.781, -78.429, 65.232, 0.4], [428.918, -77.094, 71.643, 0.4], [431.52, -77.579, 72.039, 0.4], [431.52, -77.579, 72.039, 0.4], [441.197, -79.383, 73.51, 0.4], [448.142, -83.663, 75.074, 0.4]])
        self._set_section_morphology(self.apic[73], [[207.571, -52.219, -13.205, 1.6], [208.218, -44.576, -17.861, 0.8], [208.406, -39.932, -21.972, 0.8]])
        self._set_section_morphology(self.apic[74], [[208.406, -39.932, -21.972, 0.8], [210.282, -32.666, -23.529, 0.8], [214.205, -27.09, -24.41, 0.8], [223.428, -19.511, -24.489, 0.8]])
        self._set_section_morphology(self.apic[75], [[223.428, -19.511, -24.489, 0.8], [238.336, -18.435, -22.531, 0.3], [239.284, -18.352, -22.349, 0.3], [239.284, -18.352, -22.349, 0.3], [250.056, -17.402, -20.281, 0.3], [254.951, -18.005, -19.274, 0.3], [254.951, -18.005, -19.274, 0.3], [261.026, -18.753, -18.023, 0.3], [270.57, -20.239, -16.392, 0.3], [270.57, -20.239, -16.392, 0.3], [270.926, -20.294, -16.331, 0.3], [285.912, -24.676, -14.917, 0.3], [285.912, -24.676, -14.917, 0.3], [294.355, -27.144, -14.12, 0.3], [301.186, -29.294, -13.274, 0.3], [301.186, -29.294, -13.274, 0.3], [314.271, -33.411, -11.654, 0.3], [316.455, -33.84, -11.499, 0.3], [316.455, -33.84, -11.499, 0.3], [327.567, -36.025, -10.715, 0.3], [332.222, -35.448, -10.777, 0.3], [332.222, -35.448, -10.777, 0.3], [340.704, -34.398, -10.892, 0.3], [348.041, -32.862, -10.855, 0.3], [348.041, -32.862, -10.855, 0.3], [349.701, -32.515, -10.847, 0.3], [353.367, -28.947, -9.69, 0.3], [357.267, -24.402, -7.54, 0.3], [358.429, -22.143, -6.516, 0.3], [358.429, -22.143, -6.516, 0.3]])
        self._set_section_morphology(self.apic[76], [[223.428, -19.511, -24.489, 0.8], [226.51, -11.041, -22.989, 0.3], [227.713, -5.868, -23.036, 0.3], [227.713, -5.868, -23.036, 0.3], [227.987, -4.692, -23.047, 0.3], [232.445, 2.816, -22.937, 0.3], [234.367, 6.88, -22.591, 0.3], [234.367, 6.88, -22.591, 0.3], [235.467, 9.205, -22.393, 0.3], [243.045, 18.337, -22.117, 0.3], [243.045, 18.337, -22.117, 0.3], [243.055, 18.348, -22.117, 0.3], [243.849, 25.963, -21.749, 0.3], [247.393, 31.701, -21.171, 0.3], [247.393, 31.701, -21.171, 0.3], [251.171, 37.815, -20.554, 0.3], [257.533, 41.167, -19.752, 0.3], [257.533, 41.167, -19.752, 0.3], [258.024, 41.425, -19.69, 0.3], [271.549, 44.345, -18.467, 0.3], [271.549, 44.345, -18.467, 0.3], [274.819, 45.051, -18.172, 0.3], [285.06, 46.02, -17.521, 0.3], [285.704, 46.466, -17.49, 0.3], [285.704, 46.466, -17.49, 0.3], [289.743, 49.263, -17.292, 0.3], [297.197, 54.781, -16.435, 0.3], [297.324, 54.958, -16.417, 0.3], [297.324, 54.958, -16.417, 0.3], [301.797, 61.198, -15.788, 0.3], [305.632, 65.768, -12.64, 0.3], [305.632, 65.768, -12.64, 0.3]])
        self._set_section_morphology(self.apic[77], [[208.406, -39.932, -21.972, 0.8], [207.465, -39.117, -23.557, 0.55], [206.524, -38.303, -25.142, 0.3]])
        self._set_section_morphology(self.apic[78], [[206.524, -38.303, -25.142, 0.3], [208.906, -38.547, -29.992, 0.3], [212.571, -41.823, -36.688, 0.3], [212.967, -41.711, -38.29, 0.3], [212.967, -41.711, -38.29, 0.3], [214.282, -41.339, -43.604, 0.3], [217.055, -42.235, -49.415, 0.3], [219.492, -44.187, -50.711, 0.3], [219.492, -44.187, -50.711, 0.3], [223.552, -47.44, -52.87, 0.3], [229.85, -49.962, -56.404, 0.3], [231.57, -50.744, -57.291, 0.3], [231.57, -50.744, -57.291, 0.3], [237.457, -53.422, -60.329, 0.3], [243.217, -57.296, -64.739, 0.3], [243.217, -57.296, -64.739, 0.3], [243.369, -57.398, -64.855, 0.3], [249.939, -61.06, -69.847, 0.3], [254.393, -63.631, -73.173, 0.3], [254.393, -63.631, -73.173, 0.3], [256.002, -64.559, -74.375, 0.3], [263.326, -62.162, -77.961, 0.3], [267.315, -60.169, -79.303, 0.3], [267.315, -60.169, -79.303, 0.3], [271.035, -58.31, -80.555, 0.3], [274.559, -56.821, -86.374, 0.3], [278.171, -57.441, -88.126, 0.3]])
        self._set_section_morphology(self.apic[79], [[206.524, -38.303, -25.142, 0.3], [201.146, -32.953, -29.136, 0.3], [196.664, -31.05, -31.383, 0.3], [196.664, -31.05, -31.383, 0.3], [191.718, -28.951, -33.864, 0.3], [187.418, -23.972, -38.446, 0.3], [187.418, -23.972, -38.446, 0.3], [185.527, -21.782, -40.461, 0.3], [179.288, -15.827, -46.29, 0.3], [179.288, -15.827, -46.29, 0.3], [179.002, -15.555, -46.556, 0.3], [175.267, -10.202, -51.444, 0.3], [172.561, -6.923, -54.616, 0.3], [172.561, -6.923, -54.616, 0.3], [170.612, -4.561, -56.901, 0.3], [167.158, 1.22, -63.785, 0.3], [166.914, 1.451, -64.134, 0.3], [166.914, 1.451, -64.134, 0.3], [163.037, 5.118, -69.665, 0.3], [164.144, 9.475, -73.207, 0.3], [164.462, 9.51, -73.626, 0.3], [164.462, 9.51, -73.626, 0.3], [167.778, 9.885, -77.991, 0.3], [168.156, 16.561, -83.141, 0.3]])
        self._set_section_morphology(self.apic[7], [[131.387, -27.67, -8.294, 2.2], [141.619, -31.944, -8.518, 2.2], [147.276, -34.255, -9.593, 1.8]])
        self._set_section_morphology(self.apic[80], [[186.559, -45.066, -11.255, 1.6], [198.098, -37.708, -15.186, 0.3], [202.132, -36.178, -15.136, 0.3], [202.132, -36.178, -15.136, 0.3], [209.424, -33.412, -15.047, 0.3], [220.02, -31.572, -15.101, 0.3], [220.02, -31.572, -15.101, 0.3], [224.439, -30.805, -15.124, 0.3], [235.164, -28.417, -14.978, 0.3], [238.23, -28.121, -14.993, 0.3], [238.23, -28.121, -14.993, 0.3], [247.464, -27.228, -15.04, 0.3], [256.697, -26.335, -15.086, 0.3], [256.697, -26.335, -15.086, 0.3], [264.442, -25.586, -15.125, 0.3], [275.198, -24.99, -15.248, 0.3], [275.198, -24.99, -15.248, 0.3], [284.247, -24.488, -15.351, 0.3], [293.664, -24.016, -14.274, 0.3], [293.664, -24.016, -14.274, 0.3], [304.364, -23.479, -13.05, 0.3], [312.123, -23.367, -13.459, 0.3], [312.123, -23.367, -13.459, 0.3], [317.082, -23.295, -13.72, 0.3], [326.588, -21.574, -14.139, 0.3], [330.117, -19.914, -14.516, 0.3], [330.117, -19.914, -14.516, 0.3], [335.927, -17.181, -15.136, 0.3], [340.597, -16.569, -18.853, 0.3], [346.522, -17.914, -19.433, 0.3], [346.522, -17.914, -19.433, 0.3]])
        self._set_section_morphology(self.apic[81], [[174.742, -42.389, -10.594, 1.6], [181.446, -42.086, -9.451, 1.14], [188.15, -41.783, -8.308, 0.68], [188.15, -41.783, -8.308, 0.68], [193.691, -41.533, -7.363, 0.3], [200.992, -41.509, -4.12, 0.3], [200.992, -41.509, -4.12, 0.3], [206.934, -41.49, -1.48, 0.3], [213.694, -41.428, 0.73, 0.3], [213.694, -41.428, 0.73, 0.3], [220.165, -41.369, 2.846, 0.3], [226.635, -41.31, 4.961, 0.3], [226.635, -41.31, 4.961, 0.3], [228.032, -41.298, 5.418, 0.3], [239.529, -42.285, 9.206, 0.3]])
        self._set_section_morphology(self.apic[82], [[239.529, -42.285, 9.206, 0.3], [253.798, -40.999, 13.623, 0.3], [255.6, -41.135, 14.236, 0.3], [255.6, -41.135, 14.236, 0.3], [264.819, -41.836, 17.376, 0.3], [271.538, -42.579, 19.665, 0.3], [271.538, -42.579, 19.665, 0.3], [277.71, -43.261, 21.768, 0.3], [285.518, -42.561, 25.773, 0.3], [286.884, -42.19, 26.383, 0.3], [286.884, -42.19, 26.383, 0.3], [297.167, -39.397, 30.974, 0.3], [301.026, -36.984, 33.686, 0.3], [301.026, -36.984, 33.686, 0.3], [303.314, -35.552, 35.294, 0.3], [308.462, -34.532, 41.122, 0.3], [313.323, -35.003, 44.461, 0.3]])
        self._set_section_morphology(self.apic[83], [[239.529, -42.285, 9.206, 0.3], [254.936, -46.614, 9.825, 0.3], [255.704, -46.615, 9.875, 0.3], [255.704, -46.615, 9.875, 0.3], [263.3, -46.626, 10.376, 0.3], [272.354, -45.18, 10.62, 0.3], [272.354, -45.18, 10.62, 0.3], [277.656, -44.333, 10.763, 0.3], [287.683, -40.142, 13.827, 0.3], [287.799, -40.139, 13.867, 0.3], [287.799, -40.139, 13.867, 0.3], [298.529, -39.876, 17.542, 0.3], [303.712, -39.684, 19.183, 0.3], [303.712, -39.684, 19.183, 0.3], [310.476, -39.433, 21.325, 0.3], [316.179, -39.125, 23.698, 0.3], [319.51, -40.173, 23.943, 0.3]])
        self._set_section_morphology(self.apic[84], [[161.197, -40.215, -10.035, 1.8], [161.958, -45.717, -15.364, 0.3], [162.413, -46.943, -16.164, 0.3], [162.413, -46.943, -16.164, 0.3], [163.781, -50.633, -18.574, 0.3], [165.15, -54.324, -20.984, 0.3], [165.15, -54.324, -20.984, 0.3], [165.931, -56.431, -22.36, 0.3], [169.8, -61.328, -24.491, 0.3]])
        self._set_section_morphology(self.apic[85], [[169.8, -61.328, -24.491, 0.3], [176.587, -64.537, -30.482, 0.3], [182.493, -68.423, -34.229, 0.3], [182.493, -68.423, -34.229, 0.3], [184.285, -69.602, -35.365, 0.3], [193.3, -74.037, -41.18, 0.3], [195.966, -74.742, -43.446, 0.3], [195.966, -74.742, -43.446, 0.3], [203.081, -76.625, -49.495, 0.3], [206.479, -77.193, -55.272, 0.3], [207.569, -77.402, -56.046, 0.3], [207.569, -77.402, -56.046, 0.3], [214.819, -78.794, -61.2, 0.3], [220.698, -82.759, -65.227, 0.3], [221.055, -82.943, -65.424, 0.3], [221.055, -82.943, -65.424, 0.3], [228.663, -86.857, -69.615, 0.3], [233.484, -90.541, -74.949, 0.3], [233.484, -90.541, -74.949, 0.3], [234.556, -91.36, -76.134, 0.3], [242.973, -94.028, -80.527, 0.3], [247.901, -96.776, -82.407, 0.3], [247.901, -96.776, -82.407, 0.3], [251.673, -98.879, -83.846, 0.3], [256.565, -99.92, -90.516, 0.3], [260.052, -102.598, -92.226, 0.3]])
        self._set_section_morphology(self.apic[86], [[169.8, -61.328, -24.491, 0.3], [175.29, -67.653, -23.975, 0.3], [180.779, -73.978, -23.46, 0.3], [180.779, -73.978, -23.46, 0.3], [181.694, -75.032, -23.374, 0.3], [192.071, -86.388, -23.272, 0.3], [192.071, -86.388, -23.272, 0.3], [193.803, -88.284, -23.255, 0.3], [202.775, -99.275, -22.396, 0.3], [202.775, -99.275, -22.396, 0.3], [204.745, -101.688, -22.208, 0.3], [215.512, -110.092, -22.491, 0.3], [215.512, -110.092, -22.491, 0.3], [218.264, -112.24, -22.564, 0.3], [229.104, -119.916, -22.116, 0.3], [229.104, -119.916, -22.116, 0.3], [230.265, -120.738, -22.067, 0.3], [238.877, -130.27, -22.771, 0.3], [240.302, -132.278, -22.38, 0.3], [240.302, -132.278, -22.38, 0.3], [244.62, -138.364, -21.193, 0.3], [250.689, -145.246, -20.23, 0.3], [250.689, -145.246, -20.23, 0.3], [252.299, -147.071, -19.974, 0.3], [258.969, -153.884, -18.366, 0.3], [262.385, -157.047, -18.662, 0.3], [262.385, -157.047, -18.662, 0.3], [267.556, -161.835, -19.11, 0.3], [273.547, -169.49, -19.03, 0.3], [273.547, -169.49, -19.03, 0.3]])
        self._set_section_morphology(self.apic[87], [[159.496, -38.626, -8.682, 1.8], [165.813, -46.907, -8.565, 0.3], [169.74, -51.858, -7.119, 0.3], [169.74, -51.858, -7.119, 0.3], [176.883, -60.865, -4.488, 0.3], [180.038, -64.72, -3.365, 0.3], [180.038, -64.72, -3.365, 0.3], [188.429, -74.973, -0.376, 0.3], [190.401, -77.435, 0.649, 0.3], [190.401, -77.435, 0.649, 0.3], [199.076, -88.268, 5.16, 0.3], [200.57, -89.921, 5.752, 0.3], [200.57, -89.921, 5.752, 0.3], [208.994, -99.242, 9.089, 0.3], [211.181, -102.239, 10.288, 0.3], [211.181, -102.239, 10.288, 0.3], [217.92, -111.473, 13.985, 0.3], [220.679, -115.495, 14.265, 0.3], [220.679, -115.495, 14.265, 0.3], [229.388, -128.188, 15.148, 0.3], [230.114, -129.443, 15.444, 0.3], [230.114, -129.443, 15.444, 0.3], [232.727, -133.954, 16.511, 0.3], [234.709, -144.931, 19.612, 0.3], [234.709, -144.931, 19.612, 0.3], [234.933, -146.17, 19.962, 0.3], [236.97, -159.388, 21.421, 0.3], [238.211, -160.709, 22.557, 0.3], [238.211, -160.709, 22.557, 0.3], [241.841, -164.576, 25.878, 0.3], [247.553, -168.984, 29.369, 0.3], [248.986, -170.667, 30.786, 0.3], [248.986, -170.667, 30.786, 0.3], [254.838, -177.544, 36.574, 0.3], [259.389, -180.894, 39.059, 0.3], [259.389, -180.894, 39.059, 0.3], [263.514, -183.93, 41.311, 0.3], [272.505, -189.9, 43.552, 0.3], [272.769, -189.983, 43.603, 0.3], [272.769, -189.983, 43.603, 0.3], [281.003, -192.572, 45.18, 0.3], [288.249, -195.898, 46.74, 0.3]])
        self._set_section_morphology(self.apic[88], [[152.359, -36.379, -9.207, 1.8], [152.579, -41.707, -13.573, 0.5], [152.177, -49.973, -14.902, 0.5]])
        self._set_section_morphology(self.apic[89], [[152.177, -49.973, -14.902, 0.5], [153.154, -58.138, -13.134, 0.3], [156.86, -62.974, -12.772, 0.3], [159.337, -65.428, -12.749, 0.3], [159.337, -65.428, -12.749, 0.3], [169.27, -75.272, -12.657, 0.3], [172.126, -78.092, -12.492, 0.3], [172.126, -78.092, -12.492, 0.3], [184.852, -90.663, -11.757, 0.3], [184.919, -90.729, -11.729, 0.3], [184.919, -90.729, -11.729, 0.3], [195.839, -101.448, -7.262, 0.3], [197.565, -102.106, -6.346, 0.3], [197.565, -102.106, -6.346, 0.3], [203.547, -104.386, -3.174, 0.3], [213.085, -108.062, 0.485, 0.3], [213.085, -108.062, 0.485, 0.3], [218.175, -110.023, 2.438, 0.3], [229.347, -111.745, 7.048, 0.3], [229.347, -111.745, 7.048, 0.3], [231.326, -112.05, 7.864, 0.3], [238.331, -114.248, 10.384, 0.3], [245.727, -117.097, 11.943, 0.3]])
        self._set_section_morphology(self.apic[8], [[147.276, -34.255, -9.593, 1.8], [149.817, -35.317, -9.4, 1.8], [152.359, -36.379, -9.207, 1.8]])
        self._set_section_morphology(self.apic[90], [[152.177, -49.973, -14.902, 0.5], [152.999, -56.468, -16.736, 0.426], [153.821, -62.964, -18.571, 0.351], [153.821, -62.964, -18.571, 0.351], [154.39, -67.464, -19.842, 0.3], [156.68, -75.726, -22.19, 0.3], [156.68, -75.726, -22.19, 0.3], [158.215, -81.266, -23.764, 0.3], [160.557, -88.12, -26.191, 0.3], [160.557, -88.12, -26.191, 0.3], [161.632, -91.267, -27.305, 0.3], [163.333, -100.937, -29.641, 0.3], [163.333, -100.937, -29.641, 0.3], [164.173, -105.711, -30.795, 0.3], [167.073, -113.776, -31.688, 0.3], [167.073, -113.776, -31.688, 0.3], [167.576, -115.175, -31.843, 0.3], [172.022, -126.433, -31.725, 0.3], [172.022, -126.433, -31.725, 0.3], [172.541, -127.748, -31.711, 0.3], [175.193, -139.596, -32.75, 0.3]])
        self._set_section_morphology(self.apic[91], [[147.276, -34.255, -9.593, 1.8], [152.654, -30.204, -15.353, 0.3], [161.471, -29.971, -17.665, 0.3], [161.471, -29.971, -17.665, 0.3], [161.84, -29.962, -17.762, 0.3], [177.728, -30.261, -20.718, 0.3], [179.141, -30.394, -20.921, 0.3], [179.141, -30.394, -20.921, 0.3], [189.585, -31.382, -22.417, 0.3], [196.798, -31.523, -23.982, 0.3], [196.798, -31.523, -23.982, 0.3], [200.199, -31.59, -24.72, 0.3], [211.896, -32.146, -28.949, 0.3], [213.928, -32.256, -29.175, 0.3], [213.928, -32.256, -29.175, 0.3], [225.957, -32.912, -30.511, 0.3], [231.579, -32.361, -32.062, 0.3], [231.579, -32.361, -32.062, 0.3], [234.818, -32.044, -32.956, 0.3], [242.645, -27.703, -35.053, 0.3], [245.963, -24.545, -37.934, 0.3], [245.963, -24.545, -37.934, 0.3], [247.598, -22.989, -39.354, 0.3], [256.083, -18.333, -41.916, 0.3], [258.988, -14.101, -43.236, 0.3], [258.988, -14.101, -43.236, 0.3], [262.291, -9.29, -44.736, 0.3], [270.133, -1.812, -47.911, 0.3], [270.58, -1.37, -48.12, 0.3], [270.58, -1.37, -48.12, 0.3], [278.968, 6.922, -52.054, 0.3], [283.514, 9.151, -54.315, 0.3], [283.514, 9.151, -54.315, 0.3]])
        self._set_section_morphology(self.apic[92], [[131.387, -27.67, -8.294, 2.2], [136.188, -37.067, -13.763, 0.3], [137.806, -39.397, -14.794, 0.3], [137.806, -39.397, -14.794, 0.3], [143.66, -47.826, -18.522, 0.3], [146.401, -50.32, -19.989, 0.3], [146.401, -50.32, -19.989, 0.3], [152.509, -55.875, -23.257, 0.3], [157.391, -58.835, -25.182, 0.3], [157.391, -58.835, -25.182, 0.3], [165.172, -63.553, -28.25, 0.3], [168.361, -67.686, -29.17, 0.3], [168.361, -67.686, -29.17, 0.3], [174.266, -75.34, -30.872, 0.3], [177.294, -79.344, -31.696, 0.3], [177.294, -79.344, -31.696, 0.3], [181.04, -84.297, -32.714, 0.3], [185.042, -91.849, -33.769, 0.3], [185.042, -91.849, -33.769, 0.3], [186.379, -94.372, -34.121, 0.3], [195.775, -101.531, -35.333, 0.3], [195.84, -101.647, -35.407, 0.3], [195.84, -101.647, -35.407, 0.3], [198.967, -107.269, -38.992, 0.3], [203.307, -112.629, -42.036, 0.3], [203.307, -112.629, -42.036, 0.3], [205.254, -115.033, -43.401, 0.3], [211.426, -119.612, -46.893, 0.3], [214.163, -120.999, -47.18, 0.3], [214.163, -120.999, -47.18, 0.3]])
        self._set_section_morphology(self.apic[93], [[126.356, -25.032, -7.186, 2.2], [133.155, -19.325, -10.888, 0.6], [135.751, -15.947, -10.298, 0.6]])
        self._set_section_morphology(self.apic[94], [[135.751, -15.947, -10.298, 0.6], [137.819, -6.647, -12.895, 0.6], [138.384, -2.117, -15.475, 0.6]])
        self._set_section_morphology(self.apic[95], [[138.384, -2.117, -15.475, 0.6], [135.276, 7.238, -18.915, 0.3], [132.217, 13.217, -20.135, 0.3], [132.217, 13.217, -20.135, 0.3], [128.247, 20.976, -21.718, 0.3], [124.459, 28.361, -23.06, 0.3], [124.459, 28.361, -23.06, 0.3], [124.081, 29.098, -23.193, 0.3], [117.266, 36.498, -20.314, 0.3], [112.051, 39.183, -19.235, 0.3], [112.051, 39.183, -19.235, 0.3], [106.728, 41.924, -18.133, 0.3], [101.117, 46.854, -13.61, 0.3], [100.351, 48.69, -12.186, 0.3], [100.351, 48.69, -12.186, 0.3], [98.843, 52.304, -9.382, 0.3], [95.202, 60.285, -4.303, 0.3], [94.398, 62.129, -3.161, 0.3], [94.398, 62.129, -3.161, 0.3], [92.278, 66.989, -0.148, 0.3], [87.645, 76.16, 4.228, 0.3], [87.645, 76.16, 4.228, 0.3], [87.543, 76.361, 4.323, 0.3], [82.99, 82.523, 6.881, 0.3], [76.58, 88.735, 6.307, 0.3]])
        self._set_section_morphology(self.apic[96], [[138.384, -2.117, -15.475, 0.6], [145.716, 1.849, -19.6, 0.3], [147.849, 3.108, -20.354, 0.3], [147.849, 3.108, -20.354, 0.3], [154.385, 6.969, -22.663, 0.3], [157.527, 9.205, -23.54, 0.3], [157.527, 9.205, -23.54, 0.3], [162.036, 12.414, -24.799, 0.3], [167.807, 14.445, -25.885, 0.3], [167.807, 14.445, -25.885, 0.3], [172.242, 16.006, -26.721, 0.3], [178.006, 19.955, -28.06, 0.3], [178.006, 19.955, -28.06, 0.3], [181.145, 22.105, -28.79, 0.3], [186.268, 27.822, -31.098, 0.3]])
        self._set_section_morphology(self.apic[97], [[186.268, 27.822, -31.098, 0.3], [185.662, 34.81, -35.82, 0.3], [189.458, 39.882, -39.389, 0.3], [189.458, 39.882, -39.389, 0.3], [189.781, 40.313, -39.693, 0.3], [193.633, 44.85, -44.062, 0.3], [198.243, 48.914, -48.742, 0.3], [198.243, 48.914, -48.742, 0.3], [199.31, 49.855, -49.825, 0.3], [202.887, 61.817, -54.393, 0.3], [203.167, 62.325, -54.672, 0.3], [203.167, 62.325, -54.672, 0.3], [205.838, 67.167, -57.336, 0.3], [210.868, 70.814, -60.102, 0.3], [213.214, 72.106, -60.876, 0.3], [213.214, 72.106, -60.876, 0.3], [218.728, 75.143, -62.697, 0.3], [223.509, 78.35, -63.965, 0.3], [226.437, 78.995, -65.291, 0.3]])
        self._set_section_morphology(self.apic[98], [[186.268, 27.822, -31.098, 0.3], [191.879, 27.158, -31.771, 0.3], [197.49, 26.495, -32.444, 0.3], [197.49, 26.495, -32.444, 0.3], [199.553, 26.251, -32.692, 0.3], [207.963, 25.689, -35.132, 0.3], [208.388, 25.512, -35.361, 0.3], [208.388, 25.512, -35.361, 0.3], [213.091, 23.555, -37.896, 0.3], [217.794, 21.598, -40.432, 0.3], [217.794, 21.598, -40.432, 0.3], [218.556, 21.281, -40.843, 0.3], [227.764, 18.365, -44.855, 0.3], [227.764, 18.365, -44.855, 0.3], [229.383, 17.852, -45.56, 0.3], [234.496, 18.326, -48.743, 0.3], [237.867, 18.834, -49.536, 0.3]])
        self._set_section_morphology(self.apic[99], [[135.751, -15.947, -10.298, 0.6], [139.744, -15.643, -9.05, 0.501], [143.737, -15.339, -7.802, 0.402], [143.737, -15.339, -7.802, 0.402], [147.849, -15.027, -6.517, 0.3], [151.451, -14.857, -4.629, 0.3], [151.451, -14.857, -4.629, 0.3], [156.576, -14.614, -1.942, 0.3], [159.072, -14.874, -1.271, 0.3]])
        self._set_section_morphology(self.apic[9], [[152.359, -36.379, -9.207, 1.8], [155.927, -37.502, -8.945, 1.8], [159.496, -38.626, -8.682, 1.8]])
        self._set_section_morphology(self.axon, [[-0.662, 0.337, -0.628, 1.0], [-5.279, 7.029, -2.098, 0.3], [-12.943, 12.028, -12.248, 0.3], [-16.185, 14.083, -16.521, 0.3], [-16.844, 15.488, -17.941, 0.3], [-16.844, 15.488, -17.941, 0.3], [-17.909, 17.757, -20.233, 0.3], [-19.451, 18.222, -25.86, 0.3], [-22.01, 19.011, -30.559, 0.3], [-24.31, 25.483, -35.88, 0.3], [-27.372, 28.857, -40.416, 0.3], [-27.372, 28.857, -40.416, 0.3], [-28.281, 29.858, -41.762, 0.3], [-33.468, 37.241, -46.795, 0.3], [-39.326, 45.352, -53.895, 0.3], [-41.646, 47.751, -57.969, 0.3], [-41.646, 47.751, -57.969, 0.3], [-42.938, 49.088, -60.238, 0.3], [-47.968, 58.516, -65.812, 0.3], [-53.875, 63.502, -71.335, 0.3], [-57.845, 66.497, -73.134, 0.3], [-57.845, 66.497, -73.134, 0.3], [-63.385, 70.677, -75.645, 0.3], [-70.041, 76.953, -79.745, 0.3], [-77.97, 85.606, -83.654, 0.3], [-77.97, 85.606, -83.654, 0.3], [-78.8, 86.512, -84.063, 0.3], [-93.369, 100.516, -90.377, 0.3], [-98.404, 105.327, -92.592, 0.3], [-98.404, 105.327, -92.592, 0.3], [-104.8, 111.439, -95.406, 0.3], [-112.465, 119.607, -99.117, 0.3], [-116.498, 127.154, -100.64, 0.3], [-116.498, 127.154, -100.64, 0.3], [-121.89, 137.242, -102.675, 0.3], [-126.685, 147.649, -107.254, 0.3], [-127.144, 153.071, -109.312, 0.3], [-127.144, 153.071, -109.312, 0.3], [-127.414, 156.254, -110.52, 0.3], [-130.772, 161.494, -113.876, 0.3], [-136.779, 177.323, -123.118, 0.3], [-136.779, 177.323, -123.118, 0.3], [-137.534, 179.313, -124.28, 0.3], [-140.876, 197.649, -128.958, 0.3], [-144.509, 204.759, -130.512, 0.3], [-144.509, 204.759, -130.512, 0.3], [-147.255, 210.134, -131.687, 0.3], [-157.304, 231.117, -133.864, 0.3], [-157.287, 231.331, -134.008, 0.3], [-157.287, 231.331, -134.008, 0.3], [-156.584, 240.303, -140.056, 0.3], [-155.197, 251.373, -147.252, 0.3], [-153.654, 256.563, -148.887, 0.3], [-153.654, 256.563, -148.887, 0.3], [-151.353, 264.301, -151.325, 0.3], [-142.701, 282.53, -155.21, 0.3], [-142.412, 283.201, -155.52, 0.3], [-142.412, 283.201, -155.52, 0.3], [-137.148, 295.437, -161.175, 0.3], [-131.152, 308.486, -166.462, 0.3], [-131.152, 308.486, -166.462, 0.3], [-128.742, 313.73, -168.587, 0.3], [-122.815, 335.18, -176.52, 0.3], [-122.815, 335.18, -176.52, 0.3], [-117.696, 353.707, -183.372, 0.3], [-113.849, 362.102, -184.954, 0.3], [-113.849, 362.102, -184.954, 0.3], [-104.688, 382.091, -188.722, 0.3], [-103.047, 389.029, -190.938, 0.3], [-103.047, 389.029, -190.938, 0.3], [-98.577, 407.92, -196.971, 0.3], [-94.704, 415.135, -201.681, 0.3], [-94.704, 415.135, -201.681, 0.3], [-85.606, 432.083, -212.746, 0.3], [-81.911, 438.25, -215.16, 0.3]])
        self._set_section_morphology(self.basal[0], [[0.0, 0.0, 0.0, 3.0], [-5.987, 6.759, 6.383, 3.0], [-8.672, 8.66, 8.165, 3.9]])
        self._set_section_morphology(self.basal[10], [[-135.184, 20.181, -1.447, 0.3], [-148.934, 23.975, -5.452, 0.3], [-149.22, 24.153, -5.475, 0.3], [-149.22, 24.153, -5.475, 0.3], [-155.632, 28.157, -5.995, 0.3], [-162.044, 32.16, -6.515, 0.3], [-162.044, 32.16, -6.515, 0.3], [-162.48, 32.433, -6.55, 0.3], [-169.978, 37.929, -9.684, 0.3], [-174.384, 39.648, -10.654, 0.3], [-174.384, 39.648, -10.654, 0.3], [-183.819, 43.328, -12.732, 0.3], [-186.966, 46.778, -13.906, 0.3], [-186.966, 46.778, -13.906, 0.3], [-189.179, 49.203, -14.732, 0.3], [-199.984, 53.32, -16.92, 0.3], [-199.984, 53.32, -16.92, 0.3], [-204.922, 55.201, -17.92, 0.3], [-210.674, 62.877, -19.807, 0.3], [-210.674, 62.877, -19.807, 0.3], [-213.654, 66.854, -20.784, 0.3], [-217.664, 73.347, -24.214, 0.3], [-218.721, 74.402, -25.071, 0.3], [-218.721, 74.402, -25.071, 0.3], [-225.315, 80.978, -30.418, 0.3], [-226.904, 84.571, -32.434, 0.3], [-226.904, 84.571, -32.434, 0.3], [-228.808, 88.877, -34.85, 0.3], [-228.845, 97.785, -39.08, 0.3], [-228.845, 97.785, -39.08, 0.3]])
        self._set_section_morphology(self.basal[11], [[-26.117, 3.172, 14.669, 1.0], [-30.167, 4.994, 20.372, 0.3], [-37.498, 5.501, 23.346, 0.3], [-37.498, 5.501, 23.346, 0.3], [-38.643, 5.58, 23.81, 0.3], [-44.722, 12.229, 27.759, 0.3], [-48.542, 12.713, 29.111, 0.3], [-48.542, 12.713, 29.111, 0.3], [-53.015, 13.28, 30.696, 0.3], [-60.723, 19.387, 33.047, 0.3], [-60.948, 19.516, 33.098, 0.3], [-60.948, 19.516, 33.098, 0.3], [-68.85, 24.052, 34.904, 0.3], [-73.019, 27.724, 36.788, 0.3], [-73.019, 27.724, 36.788, 0.3], [-73.496, 28.145, 37.004, 0.3], [-79.16, 32.562, 40.032, 0.3], [-83.439, 37.584, 41.131, 0.3]])
        self._set_section_morphology(self.basal[12], [[-83.439, 37.584, 41.131, 0.3], [-89.54, 40.032, 41.673, 0.3], [-96.693, 45.428, 40.569, 0.3], [-98.687, 47.632, 41.386, 0.3]])
        self._set_section_morphology(self.basal[13], [[-98.687, 47.632, 41.386, 0.3], [-101.159, 49.481, 47.193, 0.3], [-107.681, 56.266, 50.608, 0.3]])
        self._set_section_morphology(self.basal[14], [[-98.687, 47.632, 41.386, 0.3], [-109.4, 54.161, 43.529, 0.3], [-110.278, 54.794, 43.601, 0.3], [-110.278, 54.794, 43.601, 0.3], [-118.437, 60.681, 44.278, 0.3], [-121.822, 62.23, 44.478, 0.3], [-121.822, 62.23, 44.478, 0.3], [-125.815, 64.056, 44.713, 0.3], [-129.652, 68.94, 46.346, 0.3], [-132.28, 70.013, 47.297, 0.3], [-132.28, 70.013, 47.297, 0.3], [-135.375, 71.276, 48.418, 0.3], [-142.371, 78.814, 48.623, 0.3], [-142.371, 78.814, 48.623, 0.3], [-143.628, 80.168, 48.66, 0.3], [-149.324, 84.597, 52.187, 0.3], [-152.773, 86.124, 51.072, 0.3], [-152.773, 86.124, 51.072, 0.3], [-153.39, 86.398, 50.873, 0.3], [-159.174, 92.937, 50.332, 0.3], [-162.575, 95.574, 51.041, 0.3], [-162.575, 95.574, 51.041, 0.3], [-162.595, 95.59, 51.045, 0.3], [-169.947, 97.384, 51.52, 0.3], [-176.139, 97.763, 51.604, 0.3]])
        self._set_section_morphology(self.basal[15], [[-83.439, 37.584, 41.131, 0.3], [-85.524, 42.885, 41.036, 0.3], [-87.608, 48.187, 40.94, 0.3], [-87.608, 48.187, 40.94, 0.3], [-89.556, 53.14, 40.85, 0.3], [-90.396, 59.076, 41.811, 0.3], [-90.396, 59.076, 41.811, 0.3], [-91.73, 68.513, 43.339, 0.3], [-92.307, 70.054, 43.912, 0.3], [-92.307, 70.054, 43.912, 0.3], [-94.194, 75.093, 45.786, 0.3], [-96.082, 80.131, 47.66, 0.3], [-96.082, 80.131, 47.66, 0.3], [-96.189, 80.42, 47.767, 0.3], [-95.893, 87.154, 51.13, 0.3], [-97.143, 90.174, 52.478, 0.3]])
        self._set_section_morphology(self.basal[16], [[-8.672, 8.66, 8.165, 3.9], [-14.318, 19.888, 11.529, 0.8], [-18.812, 28.132, 15.041, 0.8], [-22.4, 33.457, 15.176, 0.8]])
        self._set_section_morphology(self.basal[17], [[-22.4, 33.457, 15.176, 0.8], [-29.001, 37.636, 15.642, 0.6], [-38.873, 44.945, 16.819, 0.6], [-42.476, 47.133, 18.032, 0.6]])
        self._set_section_morphology(self.basal[18], [[-42.476, 47.133, 18.032, 0.6], [-52.411, 54.971, 15.181, 0.3], [-55.032, 56.584, 14.781, 0.3], [-55.032, 56.584, 14.781, 0.3], [-66.367, 63.555, 13.051, 0.3], [-68.707, 64.781, 12.773, 0.3], [-68.707, 64.781, 12.773, 0.3], [-78.904, 70.121, 11.564, 0.3], [-82.69, 72.523, 11.167, 0.3], [-82.69, 72.523, 11.167, 0.3], [-89.45, 76.811, 10.458, 0.3], [-96.211, 81.099, 9.75, 0.3], [-96.211, 81.099, 9.75, 0.3], [-100.23, 83.648, 9.328, 0.3], [-109.835, 89.545, 8.552, 0.3], [-109.835, 89.545, 8.552, 0.3], [-110.746, 90.104, 8.479, 0.3], [-123.116, 98.575, 9.047, 0.3], [-123.116, 98.575, 9.047, 0.3], [-126.352, 100.791, 9.195, 0.3], [-135.189, 104.627, 10.024, 0.3], [-137.154, 106.068, 10.487, 0.3], [-137.154, 106.068, 10.487, 0.3], [-147.746, 113.837, 12.982, 0.3], [-150.156, 115.062, 12.905, 0.3], [-150.156, 115.062, 12.905, 0.3], [-158.595, 119.352, 12.634, 0.3], [-164.633, 122.015, 12.898, 0.3], [-164.633, 122.015, 12.898, 0.3], [-171.088, 124.863, 13.181, 0.3], [-178.384, 129.964, 11.771, 0.3], [-178.384, 129.964, 11.771, 0.3], [-184.711, 134.388, 10.548, 0.3], [-191.04, 139.229, 8.375, 0.3], [-191.04, 139.229, 8.375, 0.3], [-196.333, 143.278, 6.558, 0.3], [-203.04, 147.912, 2.366, 0.3], [-203.04, 147.912, 2.366, 0.3], [-204.651, 149.025, 1.359, 0.3], [-209.853, 156.946, -1.181, 0.3], [-211.466, 159.542, -3.857, 0.3]])
        self._set_section_morphology(self.basal[19], [[-42.476, 47.133, 18.032, 0.6], [-45.974, 52.662, 19.99, 0.474], [-49.472, 58.191, 21.949, 0.347], [-49.472, 58.191, 21.949, 0.347], [-50.775, 60.25, 22.679, 0.3], [-54.562, 70.23, 25.781, 0.3], [-54.562, 70.23, 25.781, 0.3], [-55.526, 72.771, 26.571, 0.3], [-62.008, 81.113, 28.948, 0.3]])
        self._set_section_morphology(self.basal[1], [[-8.672, 8.66, 8.165, 3.9], [-13.028, 8.465, 9.386, 1.2], [-19.51, 6.847, 12.007, 1.0], [-26.117, 3.172, 14.669, 1.0]])
        self._set_section_morphology(self.basal[20], [[-62.008, 81.113, 28.948, 0.3], [-67.295, 91.702, 31.85, 0.3], [-68.394, 93.1, 32.318, 0.3], [-68.394, 93.1, 32.318, 0.3], [-71.132, 96.586, 33.483, 0.3], [-78.051, 102.031, 36.892, 0.3], [-78.051, 102.031, 36.892, 0.3], [-78.939, 102.73, 37.33, 0.3], [-87.596, 106.526, 42.682, 0.3], [-89.289, 107.402, 43.093, 0.3], [-89.289, 107.402, 43.093, 0.3], [-95.398, 110.564, 44.576, 0.3], [-102.014, 111.606, 46.12, 0.3], [-102.103, 111.676, 46.142, 0.3], [-102.103, 111.676, 46.142, 0.3], [-109.69, 117.702, 47.972, 0.3], [-112.894, 120.179, 48.945, 0.3], [-112.894, 120.179, 48.945, 0.3], [-120.018, 125.686, 51.107, 0.3], [-124.344, 127.638, 51.524, 0.3], [-124.344, 127.638, 51.524, 0.3], [-131.593, 130.91, 52.223, 0.3], [-134.617, 133.975, 56.46, 0.3]])
        self._set_section_morphology(self.basal[21], [[-62.008, 81.113, 28.948, 0.3], [-66.704, 88.367, 30.968, 0.3], [-67.612, 89.1, 31.246, 0.3], [-67.612, 89.1, 31.246, 0.3], [-73.103, 93.536, 32.927, 0.3], [-75.348, 94.042, 34.55, 0.3], [-75.348, 94.042, 34.55, 0.3], [-78.782, 94.816, 37.033, 0.3], [-82.293, 99.074, 38.702, 0.3]])
        self._set_section_morphology(self.basal[22], [[-22.4, 33.457, 15.176, 0.8], [-25.751, 43.435, 17.719, 0.3], [-26.192, 44.102, 17.943, 0.3], [-26.192, 44.102, 17.943, 0.3], [-32.324, 53.382, 21.054, 0.3], [-32.378, 53.477, 21.062, 0.3], [-32.378, 53.477, 21.062, 0.3], [-35.242, 58.536, 21.494, 0.3], [-38.106, 63.595, 21.927, 0.3]])
        self._set_section_morphology(self.basal[23], [[-38.106, 63.595, 21.927, 0.3], [-45.121, 73.679, 24.728, 0.3], [-46.227, 75.739, 25.286, 0.3], [-46.227, 75.739, 25.286, 0.3], [-49.679, 82.168, 27.027, 0.3], [-53.13, 88.597, 28.768, 0.3], [-53.13, 88.597, 28.768, 0.3], [-53.261, 88.841, 28.834, 0.3], [-60.601, 101.431, 30.907, 0.3], [-60.601, 101.431, 30.907, 0.3], [-62.254, 104.266, 31.374, 0.3], [-68.291, 113.945, 33.923, 0.3], [-68.291, 113.945, 33.923, 0.3], [-70.812, 117.985, 34.986, 0.3], [-76.126, 126.48, 36.434, 0.3]])
        self._set_section_morphology(self.basal[24], [[-76.126, 126.48, 36.434, 0.3], [-81.793, 132.921, 36.349, 0.3], [-87.46, 139.363, 36.264, 0.3], [-87.46, 139.363, 36.264, 0.3], [-88.886, 140.984, 36.242, 0.3], [-97.721, 153.032, 37.58, 0.3], [-97.721, 153.032, 37.58, 0.3], [-98.89, 154.627, 37.757, 0.3], [-103.328, 157.604, 39.397, 0.3], [-108.376, 165.38, 41.828, 0.3], [-108.376, 165.38, 41.828, 0.3], [-112.753, 172.124, 43.935, 0.3], [-118.087, 179.144, 44.688, 0.3], [-118.087, 179.144, 44.688, 0.3], [-123.233, 185.917, 45.415, 0.3], [-129.911, 191.365, 45.641, 0.3], [-129.911, 191.365, 45.641, 0.3], [-131.611, 192.752, 45.699, 0.3], [-141.993, 196.548, 45.925, 0.3], [-145.167, 198.788, 45.492, 0.3], [-145.167, 198.788, 45.492, 0.3], [-151.375, 203.17, 44.645, 0.3], [-160.565, 205.539, 43.982, 0.3]])
        self._set_section_morphology(self.basal[25], [[-76.126, 126.48, 36.434, 0.3], [-77.099, 135.708, 39.152, 0.3], [-77.354, 137.192, 41.367, 0.3], [-77.354, 137.192, 41.367, 0.3], [-78.057, 141.283, 47.474, 0.3], [-77.38, 144.334, 51.328, 0.3], [-77.38, 144.334, 51.328, 0.3], [-77.183, 145.22, 52.447, 0.3], [-82.436, 149.512, 56.508, 0.3], [-84.17, 151.113, 58.36, 0.3]])
        self._set_section_morphology(self.basal[26], [[-38.106, 63.595, 21.927, 0.3], [-38.076, 79.322, 24.552, 0.3], [-38.239, 80.558, 24.824, 0.3], [-38.239, 80.558, 24.824, 0.3], [-40.166, 95.196, 28.037, 0.3], [-40.2, 97.233, 28.59, 0.3], [-40.2, 97.233, 28.59, 0.3], [-40.305, 103.636, 30.328, 0.3], [-37.809, 112.699, 35.194, 0.3], [-37.809, 112.699, 35.194, 0.3], [-37.51, 113.785, 35.777, 0.3], [-35.794, 118.501, 39.785, 0.3], [-39.246, 124.841, 42.41, 0.3], [-38.597, 126.143, 43.55, 0.3], [-38.597, 126.143, 43.55, 0.3], [-36.076, 131.202, 47.977, 0.3], [-30.865, 139.045, 51.465, 0.3], [-30.865, 139.045, 51.465, 0.3], [-30.597, 139.449, 51.645, 0.3], [-28.339, 143.992, 54.69, 0.3], [-31.76, 154.098, 53.104, 0.3], [-31.76, 154.098, 53.104, 0.3], [-34.492, 162.171, 51.836, 0.3], [-38.033, 170.008, 52.125, 0.3], [-38.033, 170.008, 52.125, 0.3], [-41.951, 178.679, 52.446, 0.3], [-44.12, 181.986, 53.224, 0.3], [-47.093, 184.136, 53.266, 0.3], [-47.093, 184.136, 53.266, 0.3], [-54.402, 189.42, 53.369, 0.3], [-57.206, 197.118, 52.996, 0.3], [-57.206, 197.118, 52.996, 0.3]])
        self._set_section_morphology(self.basal[27], [[0.0, 0.0, 0.0, 3.2], [-11.196, -0.017, -1.814, 3.2], [-16.046, -0.589, -2.621, 2.0], [-21.848, -0.861, -3.497, 2.0]])
        self._set_section_morphology(self.basal[28], [[-21.848, -0.861, -3.497, 2.0], [-22.75, -0.58, -4.315, 2.0], [-23.652, -0.298, -5.133, 2.0]])
        self._set_section_morphology(self.basal[29], [[-23.652, -0.298, -5.133, 2.0], [-27.204, -0.766, -8.864, 1.2], [-30.692, -1.763, -8.568, 1.2]])
        self._set_section_morphology(self.basal[2], [[-26.117, 3.172, 14.669, 1.0], [-31.155, 1.718, 13.256, 0.822], [-36.192, 0.263, 11.843, 0.644], [-36.192, 0.263, 11.843, 0.644], [-37.422, -0.092, 11.498, 0.6], [-46.68, -1.952, 10.174, 0.6], [-46.68, -1.952, 10.174, 0.6], [-49.626, -2.544, 9.752, 0.6], [-57.338, -3.785, 9.275, 0.6]])
        self._set_section_morphology(self.basal[30], [[-30.692, -1.763, -8.568, 1.2], [-36.414, -2.597, -12.934, 1.0], [-40.173, -1.948, -16.205, 1.0]])
        self._set_section_morphology(self.basal[31], [[-40.173, -1.948, -16.205, 1.0], [-45.102, -5.127, -19.961, 0.6], [-49.562, -7.882, -23.585, 0.6], [-49.562, -7.882, -23.585, 0.6], [-52.996, -10.003, -26.376, 0.6], [-59.359, -12.955, -31.052, 0.364], [-59.359, -12.955, -31.052, 0.364], [-61.099, -13.762, -32.331, 0.3], [-69.051, -17.045, -38.288, 0.3], [-69.455, -17.252, -38.627, 0.3], [-69.455, -17.252, -38.627, 0.3], [-76.052, -20.627, -44.175, 0.3], [-79.85, -21.495, -45.388, 0.3], [-79.85, -21.495, -45.388, 0.3], [-83.784, -22.394, -46.645, 0.3], [-90.448, -27.646, -49.963, 0.3]])
        self._set_section_morphology(self.basal[32], [[-90.448, -27.646, -49.963, 0.3], [-94.716, -36.795, -52.527, 0.3], [-95.523, -38.443, -54.352, 0.3], [-95.523, -38.443, -54.352, 0.3], [-96.725, -40.897, -57.07, 0.3], [-97.237, -48.084, -59.434, 0.3], [-97.317, -49.559, -59.955, 0.3], [-97.317, -49.559, -59.955, 0.3], [-97.599, -54.793, -61.8, 0.3], [-101.209, -61.062, -63.569, 0.3], [-101.209, -61.062, -63.569, 0.3], [-102.97, -64.12, -64.432, 0.3], [-107.167, -72.23, -63.508, 0.3], [-107.283, -72.382, -63.531, 0.3], [-107.283, -72.382, -63.531, 0.3], [-113.287, -80.267, -64.717, 0.3], [-114.582, -82.938, -64.148, 0.3], [-114.582, -82.938, -64.148, 0.3], [-116.591, -87.084, -63.264, 0.3], [-122.203, -93.186, -63.881, 0.3], [-122.203, -93.186, -63.881, 0.3], [-123.695, -94.809, -64.044, 0.3], [-125.046, -105.386, -62.371, 0.3]])
        self._set_section_morphology(self.basal[33], [[-90.448, -27.646, -49.963, 0.3], [-100.006, -29.88, -51.039, 0.3], [-105.481, -30.407, -51.655, 0.3], [-105.481, -30.407, -51.655, 0.3], [-110.214, -30.862, -52.188, 0.3], [-120.361, -33.842, -53.205, 0.3], [-120.361, -33.842, -53.205, 0.3], [-122.276, -34.405, -53.397, 0.3], [-134.147, -35.915, -55.645, 0.3], [-135.261, -36.429, -55.665, 0.3], [-135.261, -36.429, -55.665, 0.3], [-147.652, -42.145, -55.881, 0.3], [-149.378, -42.349, -56.168, 0.3], [-149.378, -42.349, -56.168, 0.3], [-156.928, -43.238, -57.423, 0.3], [-164.477, -44.128, -58.678, 0.3], [-164.477, -44.128, -58.678, 0.3], [-167.052, -44.432, -59.107, 0.3], [-174.45, -45.257, -62.08, 0.3], [-179.038, -45.362, -63.364, 0.3], [-179.038, -45.362, -63.364, 0.3], [-179.117, -45.364, -63.387, 0.3], [-185.677, -49.589, -63.715, 0.3], [-187.456, -56.892, -63.654, 0.3]])
        self._set_section_morphology(self.basal[34], [[-40.173, -1.948, -16.205, 1.0], [-45.751, -0.2, -18.62, 0.3], [-54.0, 2.912, -21.745, 0.3]])
        self._set_section_morphology(self.basal[35], [[-54.0, 2.912, -21.745, 0.3], [-61.866, 3.805, -25.292, 0.3], [-68.286, 4.774, -26.741, 0.3]])
        self._set_section_morphology(self.basal[36], [[-68.286, 4.774, -26.741, 0.3], [-78.987, 7.091, -28.504, 0.3], [-82.031, 7.758, -29.091, 0.3], [-82.031, 7.758, -29.091, 0.3], [-95.482, 10.705, -31.683, 0.3], [-95.725, 10.721, -31.734, 0.3], [-95.725, 10.721, -31.734, 0.3], [-106.126, 11.429, -33.905, 0.3], [-109.684, 11.712, -34.466, 0.3], [-109.684, 11.712, -34.466, 0.3], [-117.278, 12.316, -35.664, 0.3], [-123.797, 12.89, -35.399, 0.3], [-123.797, 12.89, -35.399, 0.3], [-126.508, 13.129, -35.289, 0.3], [-131.066, 11.942, -35.56, 0.3], [-137.885, 11.994, -35.508, 0.3]])
        self._set_section_morphology(self.basal[37], [[-137.885, 11.994, -35.508, 0.3], [-146.542, 8.947, -38.009, 0.3], [-150.364, 7.008, -37.21, 0.3], [-153.024, 8.087, -37.877, 0.3], [-153.024, 8.087, -37.877, 0.3], [-161.826, 11.658, -40.083, 0.3], [-166.075, 12.994, -40.897, 0.3], [-168.359, 13.223, -41.982, 0.3], [-168.359, 13.223, -41.982, 0.3], [-168.539, 13.242, -42.068, 0.3], [-177.238, 14.923, -45.188, 0.3], [-183.967, 14.75, -47.81, 0.3], [-183.967, 14.75, -47.81, 0.3], [-186.507, 14.685, -48.799, 0.3], [-191.36, 16.724, -52.677, 0.3], [-198.336, 18.221, -55.158, 0.3], [-198.336, 18.221, -55.158, 0.3], [-201.93, 18.992, -56.436, 0.3], [-207.497, 19.698, -56.318, 0.3], [-212.714, 24.483, -57.781, 0.3], [-212.77, 24.547, -57.786, 0.3], [-212.77, 24.547, -57.786, 0.3], [-217.697, 30.245, -58.25, 0.3], [-219.768, 39.274, -58.606, 0.3], [-219.768, 39.274, -58.606, 0.3], [-219.9, 39.85, -58.629, 0.3], [-215.644, 46.367, -60.012, 0.3], [-210.667, 52.671, -57.833, 0.3]])
        self._set_section_morphology(self.basal[38], [[-137.885, 11.994, -35.508, 0.3], [-145.57, 12.847, -34.531, 0.3], [-156.638, 14.235, -35.294, 0.3]])
        self._set_section_morphology(self.basal[39], [[-156.638, 14.235, -35.294, 0.3], [-165.097, 14.788, -39.373, 0.3], [-171.707, 13.889, -41.208, 0.3], [-171.707, 13.889, -41.208, 0.3], [-172.085, 13.838, -41.313, 0.3], [-183.095, 13.633, -42.534, 0.3], [-187.099, 14.48, -45.14, 0.3], [-187.099, 14.48, -45.14, 0.3], [-188.281, 14.73, -45.91, 0.3], [-196.964, 13.263, -48.45, 0.3], [-201.533, 9.815, -48.667, 0.3], [-201.533, 9.815, -48.667, 0.3], [-203.825, 8.085, -48.776, 0.3], [-210.039, 4.264, -52.099, 0.3], [-214.457, 3.667, -55.21, 0.3], [-214.457, 3.667, -55.21, 0.3], [-214.725, 3.631, -55.399, 0.3], [-221.514, 6.282, -58.918, 0.3], [-227.324, 10.726, -60.913, 0.3], [-227.606, 10.746, -61.064, 0.3], [-227.606, 10.746, -61.064, 0.3], [-233.763, 11.17, -64.355, 0.3], [-240.901, 12.461, -70.227, 0.3], [-240.901, 12.461, -70.227, 0.3], [-241.757, 12.616, -70.931, 0.3], [-243.303, 15.692, -79.629, 0.3], [-242.548, 18.582, -84.662, 0.3]])
        self._set_section_morphology(self.basal[3], [[-57.338, -3.785, 9.275, 0.6], [-65.933, -7.362, 10.802, 0.3], [-68.247, -8.215, 10.886, 0.3], [-68.247, -8.215, 10.886, 0.3], [-71.3, -9.34, 10.998, 0.3], [-72.71, -12.039, 11.472, 0.3], [-78.236, -12.655, 11.687, 0.3], [-78.236, -12.655, 11.687, 0.3], [-82.541, -13.134, 11.854, 0.3], [-89.669, -15.604, 12.448, 0.3]])
        self._set_section_morphology(self.basal[40], [[-156.638, 14.235, -35.294, 0.3], [-172.288, 16.017, -36.368, 0.3], [-173.59, 16.26, -36.512, 0.3], [-173.59, 16.26, -36.512, 0.3], [-184.6, 18.319, -37.735, 0.3], [-190.225, 19.878, -38.144, 0.3], [-190.225, 19.878, -38.144, 0.3], [-198.547, 22.185, -38.748, 0.3], [-205.929, 25.872, -40.631, 0.3], [-205.929, 25.872, -40.631, 0.3], [-207.037, 26.425, -40.914, 0.3], [-209.677, 24.102, -43.537, 0.3], [-213.947, 21.238, -47.758, 0.3], [-218.417, 21.648, -49.486, 0.3], [-218.417, 21.648, -49.486, 0.3], [-223.39, 22.104, -51.408, 0.3], [-227.677, 22.388, -56.208, 0.3], [-231.412, 21.456, -59.439, 0.3], [-231.677, 21.403, -59.571, 0.3], [-231.677, 21.403, -59.571, 0.3], [-240.589, 19.613, -64.008, 0.3], [-247.316, 18.854, -65.805, 0.3], [-247.316, 18.854, -65.805, 0.3], [-252.87, 18.228, -67.289, 0.3], [-259.967, 18.357, -70.265, 0.3], [-261.824, 18.406, -73.396, 0.3]])
        self._set_section_morphology(self.basal[41], [[-68.286, 4.774, -26.741, 0.3], [-74.175, 6.612, -31.684, 0.3], [-77.704, 7.175, -38.446, 0.3], [-78.752, 7.634, -39.414, 0.3], [-78.752, 7.634, -39.414, 0.3], [-85.984, 10.804, -46.097, 0.3], [-91.002, 12.37, -50.263, 0.3], [-91.002, 12.37, -50.263, 0.3], [-94.596, 13.491, -53.246, 0.3], [-101.149, 13.951, -62.209, 0.3], [-101.684, 14.556, -63.007, 0.3], [-101.684, 14.556, -63.007, 0.3], [-106.884, 20.444, -70.765, 0.3], [-107.475, 22.631, -76.333, 0.3], [-107.475, 22.631, -76.333, 0.3], [-107.803, 23.847, -79.43, 0.3], [-117.667, 25.881, -86.645, 0.3], [-118.569, 26.336, -87.494, 0.3], [-118.569, 26.336, -87.494, 0.3], [-125.796, 29.987, -94.297, 0.3], [-131.141, 32.638, -96.815, 0.3], [-131.141, 32.638, -96.815, 0.3], [-137.269, 35.679, -99.703, 0.3], [-143.849, 40.945, -104.356, 0.3], [-143.849, 40.945, -104.356, 0.3], [-146.941, 43.419, -106.543, 0.3], [-157.185, 49.283, -110.74, 0.3], [-157.185, 49.283, -110.74, 0.3], [-159.098, 50.377, -111.523, 0.3], [-166.666, 54.835, -118.145, 0.3], [-169.58, 56.678, -119.525, 0.3], [-169.58, 56.678, -119.525, 0.3], [-178.164, 62.107, -123.591, 0.3], [-182.872, 65.647, -125.219, 0.3], [-182.872, 65.647, -125.219, 0.3], [-187.74, 69.307, -126.903, 0.3], [-193.017, 72.009, -129.321, 0.3], [-195.016, 73.15, -132.989, 0.3], [-195.016, 73.15, -132.989, 0.3]])
        self._set_section_morphology(self.basal[42], [[-54.0, 2.912, -21.745, 0.3], [-59.452, 6.718, -24.202, 0.3], [-63.822, 10.176, -28.584, 0.3]])
        self._set_section_morphology(self.basal[43], [[-63.822, 10.176, -28.584, 0.3], [-67.483, 10.788, -33.351, 0.3], [-75.719, 14.638, -37.631, 0.3], [-75.719, 14.638, -37.631, 0.3], [-77.679, 15.554, -38.65, 0.3], [-88.34, 21.787, -44.578, 0.3], [-88.34, 21.787, -44.578, 0.3], [-89.261, 22.325, -45.091, 0.3], [-101.496, 28.157, -51.295, 0.3], [-101.496, 28.157, -51.295, 0.3], [-102.096, 28.442, -51.599, 0.3], [-111.067, 31.769, -58.285, 0.3], [-114.21, 33.403, -59.306, 0.3], [-114.21, 33.403, -59.306, 0.3], [-121.244, 37.061, -61.59, 0.3], [-127.605, 39.05, -65.718, 0.3], [-127.605, 39.05, -65.718, 0.3], [-129.955, 39.785, -67.243, 0.3], [-141.639, 44.957, -70.532, 0.3], [-141.639, 44.957, -70.532, 0.3], [-142.185, 45.199, -70.686, 0.3], [-152.297, 50.466, -74.989, 0.3], [-155.187, 51.676, -75.982, 0.3], [-155.187, 51.676, -75.982, 0.3], [-167.283, 56.742, -80.139, 0.3], [-169.27, 57.529, -81.074, 0.3], [-169.27, 57.529, -81.074, 0.3], [-173.629, 59.255, -83.124, 0.3], [-182.517, 63.081, -88.298, 0.3], [-182.517, 63.081, -88.298, 0.3], [-182.548, 63.095, -88.316, 0.3], [-188.621, 64.467, -92.759, 0.3], [-194.427, 68.767, -97.049, 0.3], [-194.427, 68.767, -97.049, 0.3], [-194.743, 69.001, -97.283, 0.3], [-200.434, 74.44, -103.805, 0.3], [-205.075, 76.738, -105.372, 0.3], [-205.075, 76.738, -105.372, 0.3], [-206.219, 77.304, -105.759, 0.3], [-213.952, 81.823, -109.887, 0.3], [-217.598, 82.96, -112.947, 0.3], [-217.598, 82.96, -112.947, 0.3], [-225.731, 85.498, -119.774, 0.3], [-227.664, 86.614, -124.44, 0.3]])
        self._set_section_morphology(self.basal[44], [[-63.822, 10.176, -28.584, 0.3], [-66.637, 18.916, -31.489, 0.3], [-69.307, 26.804, -32.606, 0.3], [-69.307, 26.804, -32.606, 0.3], [-71.996, 34.751, -33.732, 0.3], [-74.662, 43.841, -35.077, 0.3], [-74.662, 43.841, -35.077, 0.3], [-76.229, 49.183, -35.867, 0.3], [-77.524, 59.543, -38.21, 0.3], [-77.973, 61.181, -38.404, 0.3], [-77.973, 61.181, -38.404, 0.3], [-81.139, 72.733, -39.773, 0.3], [-85.01, 77.273, -40.138, 0.3], [-85.01, 77.273, -40.138, 0.3], [-90.303, 83.482, -40.638, 0.3], [-96.652, 91.0, -41.24, 0.3], [-96.652, 91.0, -41.24, 0.3], [-97.539, 92.05, -41.324, 0.3], [-111.463, 100.622, -43.953, 0.3], [-111.549, 100.656, -43.974, 0.3], [-111.549, 100.656, -43.974, 0.3], [-117.431, 103.021, -45.408, 0.3], [-122.894, 101.585, -48.739, 0.3], [-123.24, 98.012, -52.183, 0.3]])
        self._set_section_morphology(self.basal[45], [[-30.692, -1.763, -8.568, 1.2], [-35.429, 3.935, -5.511, 0.3], [-39.915, 6.395, -5.153, 0.3], [-39.915, 6.395, -5.153, 0.3], [-51.192, 12.577, -4.253, 0.3], [-51.413, 12.695, -4.286, 0.3], [-51.413, 12.695, -4.286, 0.3], [-57.158, 15.77, -5.144, 0.3], [-62.904, 18.844, -6.001, 0.3], [-62.904, 18.844, -6.001, 0.3], [-72.578, 24.022, -7.444, 0.3], [-74.461, 24.74, -7.947, 0.3], [-74.461, 24.74, -7.947, 0.3], [-80.417, 27.008, -9.537, 0.3], [-86.536, 28.931, -10.989, 0.3]])
        self._set_section_morphology(self.basal[46], [[-86.536, 28.931, -10.989, 0.3], [-95.028, 29.497, -14.569, 0.3], [-101.846, 31.638, -16.589, 0.3], [-101.846, 31.638, -16.589, 0.3], [-106.282, 33.031, -17.903, 0.3], [-116.823, 36.337, -22.13, 0.3], [-116.823, 36.337, -22.13, 0.3], [-116.994, 36.391, -22.198, 0.3], [-128.841, 39.585, -26.064, 0.3], [-132.212, 40.468, -26.982, 0.3], [-132.212, 40.468, -26.982, 0.3], [-138.851, 42.205, -28.791, 0.3], [-147.714, 45.36, -30.51, 0.3], [-147.714, 45.36, -30.51, 0.3], [-151.448, 46.69, -31.234, 0.3], [-162.646, 52.465, -32.112, 0.3], [-162.646, 52.465, -32.112, 0.3], [-164.493, 53.418, -32.257, 0.3], [-176.915, 60.718, -34.47, 0.3], [-176.915, 60.718, -34.47, 0.3], [-179.844, 62.439, -34.991, 0.3], [-186.013, 67.522, -36.524, 0.3], [-189.401, 71.141, -37.65, 0.3], [-189.401, 71.141, -37.65, 0.3], [-196.44, 78.659, -39.989, 0.3], [-201.432, 81.175, -42.427, 0.3], [-201.432, 81.175, -42.427, 0.3], [-207.437, 84.201, -45.359, 0.3], [-212.798, 91.305, -48.14, 0.3], [-212.798, 91.305, -48.14, 0.3], [-219.353, 99.991, -51.541, 0.3], [-222.349, 104.279, -52.089, 0.3], [-222.349, 104.279, -52.089, 0.3], [-225.454, 108.724, -52.657, 0.3], [-229.833, 113.783, -50.062, 0.3], [-232.562, 116.739, -50.314, 0.3], [-232.562, 116.739, -50.314, 0.3]])
        self._set_section_morphology(self.basal[47], [[-86.536, 28.931, -10.989, 0.3], [-94.662, 33.596, -9.132, 0.3], [-101.09, 37.836, -6.646, 0.3], [-101.09, 37.836, -6.646, 0.3], [-105.357, 40.651, -4.996, 0.3], [-113.877, 49.455, -4.309, 0.3], [-113.877, 49.455, -4.309, 0.3], [-114.119, 49.705, -4.29, 0.3], [-122.114, 54.321, -4.428, 0.3], [-127.325, 60.459, -4.016, 0.3], [-127.325, 60.459, -4.016, 0.3], [-133.663, 67.924, -3.515, 0.3], [-139.009, 73.621, -4.143, 0.3], [-139.009, 73.621, -4.143, 0.3], [-145.026, 80.033, -4.85, 0.3], [-151.044, 86.445, -5.557, 0.3], [-151.044, 86.445, -5.557, 0.3], [-153.21, 88.754, -5.812, 0.3], [-162.026, 100.221, -6.079, 0.3], [-162.026, 100.221, -6.079, 0.3], [-168.099, 108.122, -6.263, 0.3], [-172.035, 114.404, -4.268, 0.3], [-172.035, 114.404, -4.268, 0.3], [-173.837, 117.28, -3.355, 0.3], [-181.47, 118.646, -0.884, 0.3], [-187.33, 119.538, -1.747, 0.3], [-187.33, 119.538, -1.747, 0.3], [-187.923, 119.628, -1.834, 0.3], [-191.548, 117.616, -4.028, 0.3], [-197.65, 116.39, -4.901, 0.3], [-201.714, 111.906, -4.558, 0.3], [-201.714, 111.906, -4.558, 0.3]])
        self._set_section_morphology(self.basal[48], [[-23.652, -0.298, -5.133, 2.0], [-31.262, -10.472, -2.378, 0.3], [-32.102, -10.868, -2.634, 0.3], [-32.102, -10.868, -2.634, 0.3], [-43.285, -16.133, -6.039, 0.3], [-44.199, -16.789, -6.242, 0.3], [-44.199, -16.789, -6.242, 0.3], [-51.925, -22.33, -7.96, 0.3], [-55.758, -23.225, -9.694, 0.3]])
        self._set_section_morphology(self.basal[49], [[-55.758, -23.225, -9.694, 0.3], [-59.604, -29.868, -7.279, 0.3], [-62.494, -36.555, -8.113, 0.3], [-62.494, -36.555, -8.113, 0.3], [-66.785, -46.486, -9.351, 0.3], [-68.75, -50.522, -9.25, 0.3], [-68.75, -50.522, -9.25, 0.3], [-74.306, -61.939, -8.967, 0.3], [-75.955, -64.05, -9.024, 0.3], [-75.955, -64.05, -9.024, 0.3], [-80.688, -70.108, -9.188, 0.3], [-85.421, -76.166, -9.351, 0.3], [-85.421, -76.166, -9.351, 0.3], [-90.082, -82.133, -9.512, 0.3], [-97.221, -85.276, -9.218, 0.3], [-97.221, -85.276, -9.218, 0.3], [-100.49, -86.715, -9.083, 0.3], [-108.286, -94.743, -8.899, 0.3], [-108.779, -95.101, -8.963, 0.3], [-108.779, -95.101, -8.963, 0.3], [-120.39, -103.516, -10.484, 0.3], [-121.262, -103.916, -10.497, 0.3], [-121.262, -103.916, -10.497, 0.3], [-133.269, -109.419, -10.686, 0.3], [-135.406, -109.785, -10.632, 0.3], [-135.406, -109.785, -10.632, 0.3], [-150.52, -112.37, -10.246, 0.3], [-150.56, -112.378, -10.248, 0.3], [-150.56, -112.378, -10.248, 0.3], [-155.553, -113.406, -10.552, 0.3], [-165.12, -117.147, -10.475, 0.3], [-165.12, -117.147, -10.475, 0.3], [-171.144, -119.502, -10.427, 0.3], [-177.044, -119.737, -9.807, 0.3], [-179.931, -119.13, -9.43, 0.3], [-179.931, -119.13, -9.43, 0.3], [-182.017, -118.692, -9.157, 0.3], [-191.307, -119.961, -9.738, 0.3], [-195.066, -119.828, -10.49, 0.3], [-195.066, -119.828, -10.49, 0.3], [-202.577, -119.563, -11.993, 0.3], [-210.099, -118.772, -13.51, 0.3]])
        self._set_section_morphology(self.basal[4], [[-89.669, -15.604, 12.448, 0.3], [-97.389, -18.413, 12.509, 0.3], [-101.052, -18.306, 12.767, 0.3], [-104.502, -21.421, 10.611, 0.3], [-104.974, -21.45, 10.581, 0.3], [-104.974, -21.45, 10.581, 0.3], [-115.695, -22.091, 9.891, 0.3], [-122.333, -22.02, 8.809, 0.3], [-122.333, -22.02, 8.809, 0.3], [-126.046, -21.981, 8.204, 0.3], [-137.422, -23.115, 7.984, 0.3], [-139.703, -22.979, 7.831, 0.3], [-139.703, -22.979, 7.831, 0.3], [-145.635, -22.626, 7.432, 0.3], [-152.587, -26.2, 8.064, 0.3], [-156.271, -26.015, 7.972, 0.3], [-156.271, -26.015, 7.972, 0.3], [-164.464, -25.604, 7.769, 0.3], [-171.425, -24.461, 7.283, 0.3], [-173.582, -24.891, 7.063, 0.3], [-173.582, -24.891, 7.063, 0.3], [-183.662, -26.9, 6.035, 0.3], [-190.064, -29.608, 4.327, 0.3], [-190.064, -29.608, 4.327, 0.3], [-190.775, -29.908, 4.137, 0.3], [-193.246, -31.229, 3.505, 0.3], [-206.08, -31.397, -1.345, 0.3], [-206.169, -31.408, -1.388, 0.3], [-206.169, -31.408, -1.388, 0.3], [-210.831, -32.005, -3.648, 0.3], [-220.39, -27.954, -6.381, 0.3], [-221.544, -27.076, -6.89, 0.3], [-221.544, -27.076, -6.89, 0.3], [-227.412, -22.608, -9.48, 0.3], [-233.89, -20.046, -10.47, 0.3], [-236.195, -20.255, -11.729, 0.3], [-236.195, -20.255, -11.729, 0.3], [-239.084, -20.517, -13.307, 0.3], [-247.352, -17.93, -18.425, 0.3], [-250.239, -16.743, -21.119, 0.3], [-250.239, -16.743, -21.119, 0.3], [-252.616, -15.766, -23.336, 0.3], [-255.693, -20.057, -28.446, 0.3], [-253.536, -16.037, -33.414, 0.3], [-253.536, -16.037, -33.414, 0.3]])
        self._set_section_morphology(self.basal[50], [[-55.758, -23.225, -9.694, 0.3], [-60.887, -23.72, -13.528, 0.3], [-66.867, -26.217, -20.11, 0.3], [-66.867, -26.217, -20.11, 0.3], [-68.082, -26.725, -21.447, 0.3], [-75.811, -27.987, -28.942, 0.3], [-78.189, -27.644, -30.64, 0.3], [-78.189, -27.644, -30.64, 0.3], [-82.033, -27.091, -33.383, 0.3], [-89.275, -29.545, -38.311, 0.3], [-90.421, -30.052, -39.613, 0.3], [-90.421, -30.052, -39.613, 0.3], [-97.624, -33.24, -47.793, 0.3], [-101.088, -33.876, -50.265, 0.3], [-101.088, -33.876, -50.265, 0.3], [-106.077, -34.793, -53.825, 0.3], [-115.15, -33.025, -55.847, 0.3], [-115.15, -33.025, -55.847, 0.3], [-119.242, -32.228, -56.759, 0.3], [-127.725, -33.834, -64.189, 0.3], [-127.725, -33.834, -64.189, 0.3], [-129.701, -34.208, -65.92, 0.3], [-139.091, -41.809, -70.735, 0.3], [-139.091, -41.809, -70.735, 0.3], [-140.441, -42.902, -71.427, 0.3], [-149.676, -51.924, -76.272, 0.3], [-149.676, -51.924, -76.272, 0.3], [-149.787, -52.033, -76.33, 0.3], [-163.244, -55.934, -82.942, 0.3], [-163.244, -55.934, -82.942, 0.3], [-163.691, -56.064, -83.162, 0.3], [-176.422, -57.753, -91.187, 0.3], [-176.422, -57.753, -91.187, 0.3], [-177.814, -57.938, -92.065, 0.3], [-190.522, -61.971, -96.343, 0.3], [-190.522, -61.971, -96.343, 0.3], [-199.406, -64.791, -99.334, 0.3], [-204.653, -65.71, -101.801, 0.3], [-204.653, -65.71, -101.801, 0.3], [-207.99, -66.295, -103.371, 0.3], [-212.414, -63.855, -104.223, 0.3], [-218.468, -61.957, -106.673, 0.3]])
        self._set_section_morphology(self.basal[51], [[-21.848, -0.861, -3.497, 2.0], [-25.877, -4.799, 5.857, 0.6], [-26.66, -5.089, 6.112, 0.6], [-26.66, -5.089, 6.112, 0.6], [-35.047, -8.19, 8.845, 0.6], [-37.389, -8.709, 9.305, 0.6], [-37.389, -8.709, 9.305, 0.6], [-44.801, -10.351, 10.762, 0.6], [-47.789, -13.078, 11.133, 0.6]])
        self._set_section_morphology(self.basal[52], [[-47.789, -13.078, 11.133, 0.6], [-59.584, -25.615, 10.663, 0.4], [-60.515, -26.285, 10.618, 0.4], [-60.515, -26.285, 10.618, 0.4], [-67.697, -31.448, 10.271, 0.4], [-68.533, -34.333, 9.284, 0.4], [-74.44, -36.581, 9.933, 0.335], [-74.44, -36.581, 9.933, 0.335], [-77.571, -37.772, 10.277, 0.3], [-88.021, -37.626, 10.087, 0.3], [-92.516, -38.251, 9.806, 0.3], [-92.516, -38.251, 9.806, 0.3], [-98.412, -39.072, 9.438, 0.3], [-110.263, -42.666, 8.746, 0.3], [-110.263, -42.666, 8.746, 0.3], [-111.133, -42.93, 8.695, 0.3], [-117.942, -47.595, 9.864, 0.3], [-123.022, -48.081, 12.549, 0.3], [-125.742, -49.842, 13.416, 0.3]])
        self._set_section_morphology(self.basal[53], [[-125.742, -49.842, 13.416, 0.3], [-128.218, -55.342, 16.395, 0.3], [-128.388, -59.813, 17.575, 0.3], [-128.388, -59.813, 17.575, 0.3], [-128.691, -67.762, 19.674, 0.3], [-129.214, -70.786, 20.279, 0.3], [-129.214, -70.786, 20.279, 0.3], [-131.01, -81.176, 22.355, 0.3], [-131.351, -81.662, 22.487, 0.3], [-131.351, -81.662, 22.487, 0.3], [-137.034, -89.755, 24.674, 0.3], [-138.088, -90.355, 24.863, 0.3], [-138.088, -90.355, 24.863, 0.3], [-143.543, -93.466, 25.84, 0.3], [-147.599, -96.382, 25.645, 0.3]])
        self._set_section_morphology(self.basal[54], [[-125.742, -49.842, 13.416, 0.3], [-136.24, -52.82, 14.802, 0.3], [-139.664, -53.274, 15.469, 0.3], [-139.664, -53.274, 15.469, 0.3], [-147.931, -54.37, 17.078, 0.3], [-153.583, -56.372, 17.66, 0.3], [-153.583, -56.372, 17.66, 0.3], [-160.457, -58.806, 18.367, 0.3], [-166.839, -62.101, 18.704, 0.3], [-166.839, -62.101, 18.704, 0.3], [-169.913, -63.688, 18.866, 0.3], [-175.586, -64.514, 21.019, 0.3], [-178.378, -67.988, 23.128, 0.3], [-178.378, -67.988, 23.128, 0.3], [-181.291, -71.612, 25.328, 0.3], [-185.594, -71.295, 28.044, 0.3], [-188.514, -72.935, 30.701, 0.3], [-188.514, -72.935, 30.701, 0.3], [-189.763, -73.637, 31.837, 0.3], [-193.768, -76.04, 33.136, 0.3], [-197.739, -82.119, 36.094, 0.3], [-197.739, -82.119, 36.094, 0.3], [-198.305, -82.985, 36.515, 0.3], [-204.955, -81.931, 38.558, 0.3], [-211.071, -82.619, 40.177, 0.3]])
        self._set_section_morphology(self.basal[55], [[-47.789, -13.078, 11.133, 0.6], [-50.911, -13.145, 10.428, 0.4], [-55.619, -14.809, 10.159, 0.4]])
        self._set_section_morphology(self.basal[56], [[-55.619, -14.809, 10.159, 0.4], [-62.818, -15.148, 13.703, 0.4], [-70.165, -15.817, 15.619, 0.305], [-70.165, -15.817, 15.619, 0.305], [-70.544, -15.852, 15.718, 0.3], [-82.962, -15.082, 16.385, 0.3], [-85.756, -14.913, 16.282, 0.3], [-85.756, -14.913, 16.282, 0.3], [-99.421, -14.091, 15.779, 0.3], [-101.325, -13.696, 15.579, 0.3], [-101.325, -13.696, 15.579, 0.3], [-114.112, -11.041, 14.236, 0.3], [-116.543, -10.365, 14.32, 0.3], [-116.543, -10.365, 14.32, 0.3], [-128.157, -7.137, 14.72, 0.3], [-131.308, -5.46, 15.124, 0.3], [-131.308, -5.46, 15.124, 0.3], [-135.417, -3.273, 15.651, 0.3], [-143.963, 3.037, 18.384, 0.3], [-143.963, 3.037, 18.384, 0.3], [-144.11, 3.146, 18.431, 0.3], [-154.433, 9.024, 19.613, 0.3], [-157.338, 10.905, 20.296, 0.3], [-157.338, 10.905, 20.296, 0.3], [-165.504, 16.192, 22.218, 0.3], [-170.731, 18.496, 22.757, 0.3], [-170.731, 18.496, 22.757, 0.3], [-173.866, 19.878, 23.081, 0.3], [-183.294, 27.05, 24.791, 0.3], [-183.524, 27.122, 24.76, 0.3], [-183.524, 27.122, 24.76, 0.3], [-191.349, 29.584, 23.698, 0.3], [-196.608, 32.812, 23.273, 0.3], [-197.804, 32.794, 23.32, 0.3], [-197.804, 32.794, 23.32, 0.3], [-201.373, 32.741, 23.462, 0.3], [-205.01, 24.983, 25.417, 0.3], [-208.201, 24.277, 25.02, 0.3], [-208.201, 24.277, 25.02, 0.3], [-212.84, 23.252, 24.443, 0.3], [-217.488, 23.671, 25.129, 0.3], [-223.407, 24.362, 23.605, 0.3], [-223.407, 24.362, 23.605, 0.3], [-225.453, 24.601, 23.078, 0.3], [-231.121, 27.954, 21.621, 0.3], [-235.863, 32.588, 20.193, 0.3]])
        self._set_section_morphology(self.basal[57], [[-55.619, -14.809, 10.159, 0.4], [-66.921, -14.399, 8.402, 0.3], [-71.709, -14.597, 8.092, 0.3], [-71.709, -14.597, 8.092, 0.3], [-80.168, -14.946, 7.544, 0.3], [-87.76, -13.324, 7.556, 0.3], [-87.76, -13.324, 7.556, 0.3], [-100.849, -10.526, 7.578, 0.3], [-103.6, -9.732, 7.587, 0.3], [-103.6, -9.732, 7.587, 0.3], [-111.405, -7.48, 7.612, 0.3], [-119.21, -5.228, 7.638, 0.3], [-119.21, -5.228, 7.638, 0.3], [-120.604, -4.825, 7.642, 0.3], [-132.665, 1.591, 6.19, 0.3], [-133.635, 2.011, 6.152, 0.3], [-133.635, 2.011, 6.152, 0.3], [-146.044, 7.378, 5.67, 0.3], [-148.649, 7.987, 5.183, 0.3], [-148.649, 7.987, 5.183, 0.3], [-159.091, 10.431, 3.232, 0.3], [-163.982, 12.501, 2.606, 0.3], [-163.982, 12.501, 2.606, 0.3], [-178.406, 18.606, 0.759, 0.3], [-178.807, 18.86, 0.726, 0.3], [-178.807, 18.86, 0.726, 0.3], [-184.941, 22.76, 0.227, 0.3], [-193.488, 25.453, 0.239, 0.3], [-193.488, 25.453, 0.239, 0.3], [-198.328, 26.978, 0.245, 0.3], [-204.772, 29.528, -1.243, 0.3], [-208.55, 29.829, -2.766, 0.3], [-208.55, 29.829, -2.766, 0.3], [-209.256, 29.885, -3.051, 0.3], [-215.726, 34.015, -4.58, 0.3], [-219.77, 33.731, -0.83, 0.3], [-220.981, 33.692, 0.928, 0.3], [-220.981, 33.692, 0.928, 0.3], [-222.744, 33.636, 3.488, 0.3], [-231.013, 39.391, 4.808, 0.3], [-233.594, 40.209, 6.047, 0.3], [-233.594, 40.209, 6.047, 0.3], [-236.444, 41.112, 7.416, 0.3], [-242.795, 39.446, 8.041, 0.3], [-247.145, 43.429, 5.652, 0.3]])
        self._set_section_morphology(self.basal[5], [[-89.669, -15.604, 12.448, 0.3], [-96.911, -14.889, 13.959, 0.3], [-104.686, -14.885, 14.785, 0.3], [-104.686, -14.885, 14.785, 0.3], [-108.561, -14.883, 15.196, 0.3], [-115.686, -13.679, 17.204, 0.3], [-119.288, -12.541, 17.974, 0.3], [-119.288, -12.541, 17.974, 0.3], [-124.414, -10.922, 19.069, 0.3], [-130.229, -10.656, 20.684, 0.3], [-132.949, -12.417, 21.551, 0.3], [-133.195, -12.599, 21.76, 0.3], [-133.195, -12.599, 21.76, 0.3], [-137.419, -15.713, 25.347, 0.3], [-136.412, -18.11, 29.983, 0.3], [-137.307, -20.329, 32.646, 0.3], [-137.307, -20.329, 32.646, 0.3], [-138.093, -22.28, 34.986, 0.3], [-140.813, -24.041, 35.853, 0.3], [-145.51, -26.747, 38.116, 0.3], [-147.923, -28.169, 38.775, 0.3], [-147.923, -28.169, 38.775, 0.3], [-150.141, -29.477, 39.381, 0.3], [-152.686, -29.172, 46.725, 0.3], [-155.768, -27.683, 44.982, 0.3], [-156.454, -28.254, 45.403, 0.3], [-156.454, -28.254, 45.403, 0.3], [-158.045, -29.581, 46.382, 0.3], [-160.19, -37.814, 47.444, 0.3], [-164.512, -38.022, 48.167, 0.3]])
        self._set_section_morphology(self.basal[6], [[-57.338, -3.785, 9.275, 0.6], [-72.89, -2.04, 6.705, 0.3], [-73.523, -1.868, 6.579, 0.3], [-73.523, -1.868, 6.579, 0.3], [-84.835, 1.191, 4.336, 0.3], [-89.151, 2.67, 3.786, 0.3], [-89.151, 2.67, 3.786, 0.3], [-103.649, 7.635, 1.938, 0.3], [-104.654, 8.053, 1.861, 0.3], [-104.654, 8.053, 1.861, 0.3], [-112.265, 11.216, 1.283, 0.3], [-119.877, 14.38, 0.705, 0.3], [-119.877, 14.38, 0.705, 0.3], [-124.457, 16.283, 0.357, 0.3], [-135.184, 20.181, -1.447, 0.3]])
        self._set_section_morphology(self.basal[7], [[-135.184, 20.181, -1.447, 0.3], [-139.441, 19.948, -1.721, 0.3], [-143.697, 19.716, -1.996, 0.3]])
        self._set_section_morphology(self.basal[8], [[-143.697, 19.716, -1.996, 0.3], [-153.617, 20.731, -5.681, 0.3], [-155.869, 20.217, -6.401, 0.3], [-155.869, 20.217, -6.401, 0.3], [-161.348, 18.964, -8.152, 0.3], [-168.208, 19.107, -10.209, 0.3], [-168.208, 19.107, -10.209, 0.3], [-172.076, 19.188, -11.37, 0.3], [-180.661, 20.441, -13.804, 0.3], [-180.661, 20.441, -13.804, 0.3], [-181.435, 20.554, -14.024, 0.3], [-192.314, 20.301, -17.24, 0.3], [-193.075, 20.689, -17.49, 0.3], [-193.075, 20.689, -17.49, 0.3], [-200.295, 24.378, -19.87, 0.3], [-203.56, 25.403, -21.112, 0.3], [-204.385, 25.146, -21.53, 0.3], [-204.385, 25.146, -21.53, 0.3], [-206.917, 24.357, -22.811, 0.3], [-216.466, 26.835, -25.001, 0.3], [-216.466, 26.835, -25.001, 0.3], [-216.484, 26.84, -25.005, 0.3], [-218.124, 27.341, -29.135, 0.3], [-223.888, 31.236, -34.121, 0.3]])
        self._set_section_morphology(self.basal[9], [[-143.697, 19.716, -1.996, 0.3], [-151.358, 18.988, -0.979, 0.3], [-158.242, 20.648, -0.985, 0.3], [-158.242, 20.648, -0.985, 0.3], [-165.521, 22.403, -0.992, 0.3], [-172.808, 22.159, -0.007, 0.3], [-172.808, 22.159, -0.007, 0.3], [-173.031, 22.152, 0.024, 0.3], [-179.298, 20.987, 1.644, 0.3], [-187.245, 22.184, 1.926, 0.3], [-187.245, 22.184, 1.926, 0.3], [-188.854, 22.426, 1.983, 0.3], [-195.757, 21.977, 1.038, 0.3], [-198.494, 23.365, 1.325, 0.3], [-201.438, 23.521, 0.211, 0.3], [-201.438, 23.521, 0.211, 0.3], [-206.543, 23.793, -1.721, 0.3], [-212.878, 25.263, -2.174, 0.3], [-215.024, 27.116, -2.548, 0.3], [-215.024, 27.116, -2.548, 0.3], [-218.604, 30.209, -3.173, 0.3], [-223.304, 30.115, -3.981, 0.3], [-225.623, 32.945, -3.201, 0.3], [-226.936, 33.543, -2.607, 0.3], [-226.936, 33.543, -2.607, 0.3], [-229.41, 34.669, -1.487, 0.3], [-236.451, 36.374, 1.516, 0.3], [-237.766, 39.419, 3.862, 0.3]])
        self._set_section_morphology(self.soma, [[0.0, 0.0, 0.0, 8.93], [-0.331, 0.169, -0.314, 4.965], [-0.662, 0.337, -0.628, 1.0]])
    
    def _connect_sections(self):
        self.basal[39].connect(self.basal[38](1), 0)
        self.basal[40].connect(self.basal[38](1), 0)
        self.basal[8].connect(self.basal[7](1), 0)
        self.basal[9].connect(self.basal[7](1), 0)
        self.basal[37].connect(self.basal[36](1), 0)
        self.basal[38].connect(self.basal[36](1), 0)
        self.basal[10].connect(self.basal[6](1), 0)
        self.basal[7].connect(self.basal[6](1), 0)
        self.basal[53].connect(self.basal[52](1), 0)
        self.basal[54].connect(self.basal[52](1), 0)
        self.basal[13].connect(self.basal[12](1), 0)
        self.basal[14].connect(self.basal[12](1), 0)
        self.basal[32].connect(self.basal[31](1), 0)
        self.basal[33].connect(self.basal[31](1), 0)
        self.basal[4].connect(self.basal[3](1), 0)
        self.basal[5].connect(self.basal[3](1), 0)
        self.basal[46].connect(self.basal[45](1), 0)
        self.basal[47].connect(self.basal[45](1), 0)
        self.basal[12].connect(self.basal[11](1), 0)
        self.basal[15].connect(self.basal[11](1), 0)
        self.basal[24].connect(self.basal[23](1), 0)
        self.basal[25].connect(self.basal[23](1), 0)
        self.basal[36].connect(self.basal[35](1), 0)
        self.basal[41].connect(self.basal[35](1), 0)
        self.basal[43].connect(self.basal[42](1), 0)
        self.basal[44].connect(self.basal[42](1), 0)
        self.basal[20].connect(self.basal[19](1), 0)
        self.basal[21].connect(self.basal[19](1), 0)
        self.basal[3].connect(self.basal[2](1), 0)
        self.basal[6].connect(self.basal[2](1), 0)
        self.basal[49].connect(self.basal[48](1), 0)
        self.basal[50].connect(self.basal[48](1), 0)
        self.basal[56].connect(self.basal[55](1), 0)
        self.basal[57].connect(self.basal[55](1), 0)
        self.basal[35].connect(self.basal[34](1), 0)
        self.basal[42].connect(self.basal[34](1), 0)
        self.basal[52].connect(self.basal[51](1), 0)
        self.basal[55].connect(self.basal[51](1), 0)
        self.basal[18].connect(self.basal[17](1), 0)
        self.basal[19].connect(self.basal[17](1), 0)
        self.basal[31].connect(self.basal[30](1), 0)
        self.basal[34].connect(self.basal[30](1), 0)
        self.basal[23].connect(self.basal[22](1), 0)
        self.basal[26].connect(self.basal[22](1), 0)
        self.basal[30].connect(self.basal[29](1), 0)
        self.basal[45].connect(self.basal[29](1), 0)
        self.basal[11].connect(self.basal[1](1), 0)
        self.basal[2].connect(self.basal[1](1), 0)
        self.basal[29].connect(self.basal[28](1), 0)
        self.basal[48].connect(self.basal[28](1), 0)
        self.basal[17].connect(self.basal[16](1), 0)
        self.basal[22].connect(self.basal[16](1), 0)
        self.basal[28].connect(self.basal[27](1), 0)
        self.basal[51].connect(self.basal[27](1), 0)
        self.basal[16].connect(self.basal[0](1), 0)
        self.basal[1].connect(self.basal[0](1), 0)
        self.axon.connect(self.soma(1), 0)
        self.apic[131].connect(self.apic[130](1), 0)
        self.apic[132].connect(self.apic[130](1), 0)
        self.apic[0].connect(self.soma(0), 0)
        self.apic[129].connect(self.soma(0), 0)
        self.basal[0].connect(self.soma(0), 0)
        self.basal[27].connect(self.soma(0), 0)
        self.apic[130].connect(self.apic[129](1), 0)
        self.apic[133].connect(self.apic[129](1), 0)
        self.apic[122].connect(self.apic[0](1), 0)
        self.apic[1].connect(self.apic[0](1), 0)
        self.apic[123].connect(self.apic[122](1), 0)
        self.apic[128].connect(self.apic[122](1), 0)
        self.apic[113].connect(self.apic[1](1), 0)
        self.apic[2].connect(self.apic[1](1), 0)
        self.apic[110].connect(self.apic[109](1), 0)
        self.apic[111].connect(self.apic[109](1), 0)
        self.apic[114].connect(self.apic[113](1), 0)
        self.apic[119].connect(self.apic[113](1), 0)
        self.apic[120].connect(self.apic[119](1), 0)
        self.apic[121].connect(self.apic[119](1), 0)
        self.apic[109].connect(self.apic[108](1), 0)
        self.apic[112].connect(self.apic[108](1), 0)
        self.apic[115].connect(self.apic[114](1), 0)
        self.apic[118].connect(self.apic[114](1), 0)
        self.apic[108].connect(self.apic[2](1), 0)
        self.apic[3].connect(self.apic[2](1), 0)
        self.apic[124].connect(self.apic[123](1), 0)
        self.apic[127].connect(self.apic[123](1), 0)
        self.apic[116].connect(self.apic[115](1), 0)
        self.apic[117].connect(self.apic[115](1), 0)
        self.apic[107].connect(self.apic[3](1), 0)
        self.apic[4].connect(self.apic[3](1), 0)
        self.apic[125].connect(self.apic[124](1), 0)
        self.apic[126].connect(self.apic[124](1), 0)
        self.apic[102].connect(self.apic[4](1), 0)
        self.apic[5].connect(self.apic[4](1), 0)
        self.apic[103].connect(self.apic[102](1), 0)
        self.apic[106].connect(self.apic[102](1), 0)
        self.apic[6].connect(self.apic[5](1), 0)
        self.apic[93].connect(self.apic[5](1), 0)
        self.apic[104].connect(self.apic[103](1), 0)
        self.apic[105].connect(self.apic[103](1), 0)
        self.apic[7].connect(self.apic[6](1), 0)
        self.apic[92].connect(self.apic[6](1), 0)
        self.apic[94].connect(self.apic[93](1), 0)
        self.apic[99].connect(self.apic[93](1), 0)
        self.apic[95].connect(self.apic[94](1), 0)
        self.apic[96].connect(self.apic[94](1), 0)
        self.apic[8].connect(self.apic[7](1), 0)
        self.apic[91].connect(self.apic[7](1), 0)
        self.apic[89].connect(self.apic[88](1), 0)
        self.apic[90].connect(self.apic[88](1), 0)
        self.apic[88].connect(self.apic[8](1), 0)
        self.apic[9].connect(self.apic[8](1), 0)
        self.apic[100].connect(self.apic[99](1), 0)
        self.apic[101].connect(self.apic[99](1), 0)
        self.apic[10].connect(self.apic[9](1), 0)
        self.apic[87].connect(self.apic[9](1), 0)
        self.apic[11].connect(self.apic[10](1), 0)
        self.apic[84].connect(self.apic[10](1), 0)
        self.apic[85].connect(self.apic[84](1), 0)
        self.apic[86].connect(self.apic[84](1), 0)
        self.apic[12].connect(self.apic[11](1), 0)
        self.apic[81].connect(self.apic[11](1), 0)
        self.apic[97].connect(self.apic[96](1), 0)
        self.apic[98].connect(self.apic[96](1), 0)
        self.apic[13].connect(self.apic[12](1), 0)
        self.apic[80].connect(self.apic[12](1), 0)
        self.apic[78].connect(self.apic[77](1), 0)
        self.apic[79].connect(self.apic[77](1), 0)
        self.apic[14].connect(self.apic[13](1), 0)
        self.apic[73].connect(self.apic[13](1), 0)
        self.apic[74].connect(self.apic[73](1), 0)
        self.apic[77].connect(self.apic[73](1), 0)
        self.apic[75].connect(self.apic[74](1), 0)
        self.apic[76].connect(self.apic[74](1), 0)
        self.apic[15].connect(self.apic[14](1), 0)
        self.apic[72].connect(self.apic[14](1), 0)
        self.apic[82].connect(self.apic[81](1), 0)
        self.apic[83].connect(self.apic[81](1), 0)
        self.apic[16].connect(self.apic[15](1), 0)
        self.apic[69].connect(self.apic[15](1), 0)
        self.apic[70].connect(self.apic[69](1), 0)
        self.apic[71].connect(self.apic[69](1), 0)
        self.apic[17].connect(self.apic[16](1), 0)
        self.apic[68].connect(self.apic[16](1), 0)
        self.apic[18].connect(self.apic[17](1), 0)
        self.apic[65].connect(self.apic[17](1), 0)
        self.apic[19].connect(self.apic[18](1), 0)
        self.apic[64].connect(self.apic[18](1), 0)
        self.apic[20].connect(self.apic[19](1), 0)
        self.apic[63].connect(self.apic[19](1), 0)
        self.apic[66].connect(self.apic[65](1), 0)
        self.apic[67].connect(self.apic[65](1), 0)
        self.apic[21].connect(self.apic[20](1), 0)
        self.apic[62].connect(self.apic[20](1), 0)
        self.apic[22].connect(self.apic[21](1), 0)
        self.apic[61].connect(self.apic[21](1), 0)
        self.apic[23].connect(self.apic[22](1), 0)
        self.apic[60].connect(self.apic[22](1), 0)
        self.apic[24].connect(self.apic[23](1), 0)
        self.apic[59].connect(self.apic[23](1), 0)
        self.apic[25].connect(self.apic[24](1), 0)
        self.apic[56].connect(self.apic[24](1), 0)
        self.apic[57].connect(self.apic[56](1), 0)
        self.apic[58].connect(self.apic[56](1), 0)
        self.apic[26].connect(self.apic[25](1), 0)
        self.apic[55].connect(self.apic[25](1), 0)
        self.apic[27].connect(self.apic[26](1), 0)
        self.apic[54].connect(self.apic[26](1), 0)
        self.apic[28].connect(self.apic[27](1), 0)
        self.apic[53].connect(self.apic[27](1), 0)
        self.apic[29].connect(self.apic[28](1), 0)
        self.apic[48].connect(self.apic[28](1), 0)
        self.apic[30].connect(self.apic[29](1), 0)
        self.apic[47].connect(self.apic[29](1), 0)
        self.apic[31].connect(self.apic[30](1), 0)
        self.apic[40].connect(self.apic[30](1), 0)
        self.apic[32].connect(self.apic[31](1), 0)
        self.apic[37].connect(self.apic[31](1), 0)
        self.apic[49].connect(self.apic[48](1), 0)
        self.apic[50].connect(self.apic[48](1), 0)
        self.apic[33].connect(self.apic[32](1), 0)
        self.apic[36].connect(self.apic[32](1), 0)
        self.apic[41].connect(self.apic[40](1), 0)
        self.apic[44].connect(self.apic[40](1), 0)
        self.apic[51].connect(self.apic[50](1), 0)
        self.apic[52].connect(self.apic[50](1), 0)
        self.apic[38].connect(self.apic[37](1), 0)
        self.apic[39].connect(self.apic[37](1), 0)
        self.apic[34].connect(self.apic[33](1), 0)
        self.apic[35].connect(self.apic[33](1), 0)
        self.apic[45].connect(self.apic[44](1), 0)
        self.apic[46].connect(self.apic[44](1), 0)
        self.apic[42].connect(self.apic[41](1), 0)
        self.apic[43].connect(self.apic[41](1), 0)
    
    def _discretize_model(self):
        self.soma.nseg = 1
        self.axon.nseg = 19
        for i in [25, 50, 65, 84, 99, 108, 109, 123, 124, 129, 130]:
            self.apic[i].nseg = 3
        for i in [34, 35, 37, 40, 42, 44, 46, 49, 54, 57, 66, 67, 70, 71, 81, 82, 83, 96, 97, 98, 101, 105, 110, 111, 112, 116, 117, 119, 121, 126, 132]:
            self.apic[i].nseg = 5
        for i in [33, 43, 47, 48, 58, 61, 78, 79, 85, 89, 90, 95, 104, 118, 120, 125, 131, 133]:
            self.apic[i].nseg = 7
        for i in [55, 59, 63, 75, 76, 80, 86, 91, 92, 100, 127, 128]:
            self.apic[i].nseg = 9
        for i in [38, 39, 41, 51, 52, 53, 60, 62, 64, 68, 106, 107]:
            self.apic[i].nseg = 11
        for i in [36, 72, 87]:
            self.apic[i].nseg = 13
        for i in [2, 3, 19, 21, 22, 25, 48, 51]:
            self.basal[i].nseg = 3
        for i in [6, 11, 15, 23, 31, 36, 45, 52, 53]:
            self.basal[i].nseg = 5
        for i in [5, 8, 9, 14, 20, 24, 32, 33, 37, 39, 40, 44, 54]:
            self.basal[i].nseg = 7
        for i in [10, 26, 47]:
            self.basal[i].nseg = 9
        for i in [4, 41, 46]:
            self.basal[i].nseg = 11
        for i in [18, 43, 49, 50, 56, 57]:
            self.basal[i].nseg = 13

if __name__ == '__main__':
    # if this file is run directly, create one instance
    # NB: this won't do anything interesting by itself and is best used with
    #     NEURON's GUI tools
    
    from neuron import h, gui
    h.celsius = 35
    cell = Morse_et_al_2010(name='neuron')
