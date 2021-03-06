#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy.random as random

class MarkovChain:
    """Simple Markov Chain Model.
    Parameters
    ----------
    n : int
        Number of states.
    p : list, len (n)
        Base probabilities.
    T : list of list, shape (n, n)
        Transition probabilities
    states : list, len (n), optional
        List of string labels for the states.
    verbose : bool, optional
        When ``True`` per-iteration convergence reports are printed
        to :data:`sys.stderr`. You can diagnose convergence via the
        :attr:`monitor_` attribute.
    Attributes
    ----------
    stat : int
        Dimensionality of the Gaussian emissions.
    Examples
    --------
    >>> mc = MarkovChain(n=2, P = [0.3,0.7], T =[[0.2,0.5],[0.8,0.5]],
                             states = ['Rain','Sunny'])
    ...                             #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    >>> mc.move()
    >>> mc.get_state()
    'Sunny'
    """

    def __init__(self, n, P, T, states=None, verbose= False):
        """Simple Markov chain model.

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

    def check_state(self):
        state = self.states[self.state] if self.states else self.state
        if self.verbose:
            print 'Current State: %s' % (state)

    def set_state(self, state):
        """Set the state for the MarkovChain to the specified state.
        Can be used for initialization.

        Parameters
        ----------
        state : int, or string
            the state to set; can be either the index of the state,
            or its string label, if labels have been provided at initialization
            time.
        Returns
        -------
        None
        """
        self.state = self.states.index(state) if self.states else state
        if self.verbose:
            state = self.states[self.state] if self.states else self.state
            print 'State is now: %s' % (state)

    def get_state(self):
        """Get the state of the markov chain.

        Parameters
        ----------

        Returns
        -------
        state : int, or string
            the current state to of the Markov Chain; can be either the index of the state,
            or its string label, if labels have been provided at initialization
            time.
        """
        state = self.states[self.state] if self.states else self.state
        return state

    def move(self):
        """Sample num_samples samples from the Markov Model.

        Parameters
        ----------

        Returns
        -------
        mutated : boolean
           true if the the model state has changed during the current update.

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

    Parameters
    ----------
    nucleotide: string, must be one of ['A', 'C', 'G', 'T']
        A nucleotide used to initialize the model.

    Returns
    -------
    mc : MarkovChain object.
       The MarkovChain object, using a Jukes Cantor Model initialized to the provided
       nucleotide.

    Examples
    --------
    >>> nuc_mc = JC69('A')
    <__main__.MarkovChain instance at 0x1a22066638>
    ...                             #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    >>> nuc_mc.get_state()
    'A'
    >>> nuc_mc.move()
    'True'
    >>> nuc_mc.get_state()
    'C'
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

#plot della distribuzione

def plot_gen(total_arr):
    total_v = total_arr.mean(axis=0)

    fig = plt.figure()
    ax = plt.plot(total_v,range(length*5))
    plt.plot(range(length),range(length))
    plt.plot([75,75],[0,500],'--')
    c_p = np.linspace(0,0.75,750,endpoint=False)
    k_p = -3./4 * np.log(1- 4./3 *c_p)
    plt.plot(c_p*length,k_p*length)
    plt.xlabel('c')
    plt.ylabel('k')
    return plt
