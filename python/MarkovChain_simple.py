#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:59:19 2017

@author: marcobarsacchi
"""
import numpy.random as random

class MarkovChain(object):
    """Simple Markov Chain Model.
    
    """

    def __init__(self, n, P, T, states=None, verbose= False):
        """Initialize a simple Markov Chain.
        
        """
        assert len(P) == n, "Probability vector should be of size %d" %n
        assert len(T) == len(T[0]) and len(T) == n, "Transition matrix should be of size %d" %n
        assert states is None or len(states) == n, "States vector should be of size $d" %n
        
        # Number of states of the MarkovChain
        self.n = n
        self.states = states
        self.p = P
        self.T = T
        self.state = random.choice(range(self.n),1,p=self.p)[0]
        self.verbose = verbose
        

    def set_state(self, state):
        """Set the state for the MarkovChain to the specified state.
        Can be used for initialization.
        """
        self.state = self.states.index(state) if self.states else state
        if self.verbose:
            state = self.states[self.state] if self.states else self.state
            print 'State is now: %s' % (state)
        
    def get_state(self):
        """Get the state of the markov chain. 
        Returns the state of the chain
        """
        state = self.states[self.state] if self.states else self.state
        return state
        
    def move(self):
        """Move the chain of one step.
        Returns true if the state is changed
           
        """
        current_state = self.state
        self.state = random.choice(range(self.n),1,p=self.T[current_state])[0]
        state = self.states[self.state] if self.states else self.state
        if self.verbose:
            print 'New State: %s' % (state)
        return self.state != current_state
        
        
# Jukes e Cantor
# alpha < 1/3.
def JC69(nucleotide):
    """Initialize a Markov Chain for a nucleotide, using a Jukes e Cantor model.
    
    """
    n = 4 
    prob = [0.25, 0.25, 0.25, 0.25]
    alpha = 0.005
    JC69_sub = [[1-alpha*3, alpha, alpha, alpha],
                [alpha, 1-alpha*3, alpha, alpha],
                [alpha, alpha, 1-alpha*3, alpha],
                [alpha, alpha, alpha, 1-alpha*3]]
    states = list('ACGT')
    mc = MarkovChain(n, prob, JC69_sub, states = states)
    mc.set_state(nucleotide)
    return mc
