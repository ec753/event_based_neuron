NEURON {
	ARTIFICIAL_CELL nInputs40
	POINTER on_event
}

ASSIGNED {
    on_event
	last_spike (ms)
    next_spike (ms)
    e0 (ms)
    e1 (ms)
    e2 (ms)
    e3 (ms)
	e4 (ms)
    e5 (ms)
    e6 (ms)
    e7 (ms)
	e8 (ms)
    e9 (ms)
    e10 (ms)
    e11 (ms)
	e12 (ms)
    e13 (ms)
    e14 (ms)
    e15 (ms)
	e16 (ms)
    e17 (ms)
    e18 (ms)
    e19 (ms)
	e20 (ms)
    e21 (ms)
    e22 (ms)
    e23 (ms)
	e24 (ms)
    e25 (ms)
    e26 (ms)
    e27 (ms)
	e28 (ms)
    e29 (ms)
	e30 (ms)
    e31 (ms)
    e32 (ms)
    e33 (ms)
	e34 (ms)
    e35 (ms)
    e36 (ms)
    e37 (ms)
	e38 (ms)
    e39 (ms)
	e40 (ms)
    e41 (ms)
    e42 (ms)
    e43 (ms)
	e44 (ms)
    e45 (ms)
    e46 (ms)
    e47 (ms)
	e48 (ms)
    e49 (ms)
    i0 (ms)
    i1 (ms)
    i2 (ms)
    i3 (ms)
    i4 (ms)
    i5 (ms)
    i6 (ms)
    i7 (ms)
	i8 (ms)
    i9 (ms)
    i10 (ms)
    i11 (ms)
	i12 (ms)
    i13 (ms)
    i14 (ms)
    i15 (ms)
	i16 (ms)
    i17 (ms)
    i18 (ms)
    i19 (ms)
	i20 (ms)
    i21 (ms)
    i22 (ms)
    i23 (ms)
    i24 (ms)
    i25 (ms)
    i26 (ms)
    i27 (ms)
	i28 (ms)
    i29 (ms)
	i30 (ms)
    i31 (ms)
    i32 (ms)
    i33 (ms)
    i34 (ms)
    i35 (ms)
    i36 (ms)
    i37 (ms)
	i38 (ms)
    i39 (ms)
	i40 (ms)
    i41 (ms)
    i42 (ms)
    i43 (ms)
    i44 (ms)
    i45 (ms)
    i46 (ms)
    i47 (ms)
	i48 (ms)
    i49 (ms)
}

INITIAL {
	last_spike = -INFINITY
    e0 = -INFINITY
    e1 = -INFINITY
    e2 = -INFINITY
    e3 = -INFINITY
	e4 = -INFINITY
    e5 = -INFINITY
    e6 = -INFINITY
    e7 = -INFINITY
	e8 = -INFINITY
	e9 = -INFINITY
	e10 = -INFINITY
    e11 = -INFINITY
    e12 = -INFINITY
    e13 = -INFINITY
	e14 = -INFINITY
    e15 = -INFINITY
    e16 = -INFINITY
    e17 = -INFINITY
	e18 = -INFINITY
	e19 = -INFINITY
	e20 = -INFINITY
    e21 = -INFINITY
    e22 = -INFINITY
    e23 = -INFINITY
	e24 = -INFINITY
    e25 = -INFINITY
    e26 = -INFINITY
    e27 = -INFINITY
	e28 = -INFINITY
	e29 = -INFINITY
	e30 = -INFINITY
    e31 = -INFINITY
    e32 = -INFINITY
    e33 = -INFINITY
	e34 = -INFINITY
    e35 = -INFINITY
    e36 = -INFINITY
    e37 = -INFINITY
	e38 = -INFINITY
	e39 = -INFINITY
	e40 = -INFINITY
    e41 = -INFINITY
    e42 = -INFINITY
    e43 = -INFINITY
	e44 = -INFINITY
    e45 = -INFINITY
    e46 = -INFINITY
    e47 = -INFINITY
	e48 = -INFINITY
	e49 = -INFINITY
    i0 = -INFINITY
    i1 = -INFINITY
    i2 = -INFINITY
    i3 = -INFINITY
    i4 = -INFINITY
    i5 = -INFINITY
    i6 = -INFINITY
    i7 = -INFINITY
	i8 = -INFINITY
    i9 = -INFINITY
    i10 = -INFINITY
    i11 = -INFINITY
    i12 = -INFINITY
    i13 = -INFINITY
    i14 = -INFINITY
    i15 = -INFINITY
	i16 = -INFINITY
    i17 = -INFINITY
    i18 = -INFINITY
    i19 = -INFINITY
	i20 = -INFINITY
    i21 = -INFINITY
    i22 = -INFINITY
    i23 = -INFINITY
    i24 = -INFINITY
    i25 = -INFINITY
    i26 = -INFINITY
    i27 = -INFINITY
	i28 = -INFINITY
    i29 = -INFINITY
    i30 = -INFINITY
    i31 = -INFINITY
    i32 = -INFINITY
    i33 = -INFINITY
    i34 = -INFINITY
    i35 = -INFINITY
	i36 = -INFINITY
    i37 = -INFINITY
    i38 = -INFINITY
    i39 = -INFINITY
	i40 = -INFINITY
    i41 = -INFINITY
    i42 = -INFINITY
    i43 = -INFINITY
    i44 = -INFINITY
    i45 = -INFINITY
	i46 = -INFINITY
    i47 = -INFINITY
    i48 = -INFINITY
    i49 = -INFINITY
}


NET_RECEIVE (w) {
    if (flag == 1) {
        if (next_spike == t) {
            : output a spike
            net_event(t)
            last_spike = t
        }
    } else {
        if (w > 0) {
            : excitatory input
			e49 = e48
            e48 = e47
            e47 = e46
            e46 = e45
            e45 = e44
			e44 = e43
            e43 = e42
            e42 = e41
            e41 = e40
			e40 = e39
			e39 = e38
            e38 = e37
            e37 = e36
            e36 = e35
            e35 = e34
			e34 = e33
            e33 = e32
            e32 = e31
            e31 = e30
            e30 = e29
			e29 = e28
            e28 = e27
            e27 = e26
            e26 = e25
            e25 = e24
			e24 = e23
            e23 = e22
            e22 = e21
            e21 = e20
            e20 = e19
            e19 = e18
            e18 = e17
            e17 = e16
            e16 = e15
            e15 = e14
			e14 = e13
            e13 = e12
            e12 = e11
            e11 = e10
            e10 = e9
            e9 = e8
            e8 = e7
			e7 = e6
            e6 = e5
            e5 = e4
            e4 = e3
            e3 = e2
            e2 = e1
            e1 = e0
            e0 = t
        }
        if (w < 0) {
            : inhibitory input
			i49 = i48
            i48 = i47
            i47 = i46
            i46 = i45
            i45 = i44
			i44 = i43
            i43 = i42
            i42 = i41
            i41 = i40
            i40 = i39
			i39 = i38
            i38 = i37
            i37 = i36
            i36 = i35
            i35 = i34
			i34 = i33
            i33 = i32
            i32 = i31
            i31 = i30
            i30 = i29
			i29 = i28
            i28 = i27
            i27 = i26
            i26 = i25
            i25 = i24
			i24 = i23
            i23 = i22
            i22 = i21
            i21 = i20
            i20 = i19
			i19 = i18
            i18 = i17
            i17 = i16
            i16 = i15
            i15 = i14
			i14 = i13
            i13 = i12
            i12 = i11
            i11 = i10
            i10 = i9
            i9 = i8
            i8 = i7
			i7 = i6
            i6 = i5
            i5 = i4
            i4 = i3
            i3 = i2
            i2 = i1
            i1 = i0
            i0 = t
        }
        VERBATIM
        double (*event_callback)(double, ...) = (double (*)(double, ...)) &on_event;
        double time_to_spike = event_callback(last_spike,
			e0,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,
			i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,i31,i32,i33,i34,i35,i36,i37,i38,i39,i40,i41,i42,i43,i44,i45,i46,i47,i48,i49);
		ENDVERBATIM
        : send a self-event after the predicted delay (with flag of 1)
        net_send(time_to_spike, 1)
        next_spike = time_to_spike + t
    }
}