NEURON {
	ARTIFICIAL_CELL ebneuron
	POINTER on_event
}

ASSIGNED {
    on_event
    next_spike  (ms)
	stim_times[1500] : 50 stimuli * 30 stimuli types
}

INITIAL {
	LOCAL i
	FROM i=0 TO 50*30 - 1 { 		: THE MINUS 1 IS NECESSARY FOR REASONS
        stim_times[i] = -INFINITY
    }
	
}

NET_RECEIVE (w) {
	LOCAL i
    if (flag == 1) {
        if (next_spike == t) {
            : output a spike
            net_event(t)
        }
    } else {
        FROM i=1 TO 50-1 {
            stim_times[(w*50)-i] = stim_times[((w)*50)-(i+1)] : w is 1 indexed
        }
        stim_times[(w - 1) * 50] = t
        VERBATIM
        double (*event_callback)(double*) = (double (*)(double*)) _p_on_event;
        double time_to_spike = event_callback(stim_times);
		ENDVERBATIM
        : send a self-event after the predicted delay (with flag of 1)
        : printf("time to spike %g\n", time_to_spike)
        : printf("w %g %g", ((w+1)*50)-0, ((w+1)*50)-(49+1))
        : printf("w %g t %g\n", w, t)
        net_send(time_to_spike, 1)
        next_spike = time_to_spike + t
    }
}

PROCEDURE print() {
    LOCAL i, stimid
    FROM stimid=1 TO 30 {
        printf("%g: ", stimid)
        FROM i=0 TO 50 - 1 {
            printf("%g ", stim_times[i + (stimid - 1) * 50])
        }
        printf("\n")
    }
}
