__all__ = ['Airline_alloc']

import numpy as np

from openmdao.main.api import Assembly, Component

from openmdao.lib.datatypes.api import Array, Float, Int

class ArrayFilter(Component):
	ac_ind = Array(iotype='in', desc="aircraft index")
	route_ind = Array(iotype='in', desc="route index")
	
	original = Array(iotype='in')
	filtered = Array(iotype='out')
	
	def execute(self):
		array_out = np.empty()
		temp_in = self.original
		
		for kk, kk_value in np.ndenuerate(array):
			ta = np.empty();
			
			for jj, jj_value in np.ndenumerate(array):
				ta = np.concatenate(ta, temp_in[ac_ind[kk], route_ind[jj]])
			
			array_out = np.concatenate(array_out, ta)
			
		self.filtered = array_out

class RangeExtract(Component):
	RVector = Array(iotype='in')
	distance = Array(iotype='in')
	
	ind = Array(iotype='out')
	
	def execute(self):
		ind = np.zeros(len(self.distance))
		
		for cc in xrange(len(self.distance)):
			_range = self.distance[cc]
			diff_min = inf
			
			for ii, ii_value in np.ndenumerate(self.RVector):
				diff = np.abs(ii_value - _range)
				if diff < diff_min:
					
				ind[cc] = ii[0]
				diff_min = diff
				
class OverrideFunction_Init(Component):
	ac_ind = Array(iotype='in', desc='aircraft indices')
	distance = Array(iotype='in', desc='route distance')
	DVector = Array(iotype='in', desc='route demand')
	ACNum = Array(iotype='in', desc='number of aircraft')
	RVector_in = Array(iotype='in')
	AvailPax_in = Array(iotype='in')
	route_ind = Array(iotype='in', desc='route indices')
	MH_in = Array(iotype='in')
	
	#Filtered Inputs
	RVector_out = Array(iotype='out')
	AvailPax_out = Array(iotype='out')
	TurnAround = Int(iotype='out')
	J = Array(iotype='out', desc="Number of routes")
	K = Array(iotype='out', desc="Number of aircraft types")
	Lim = Array(iotype='out')
	
	#Constants
	Runway_out = Array(iotype='out')
	MH_out = Array(iotype='out')
	FuelCost = Float(iotype='out')
	demfac = Int(iotype='out')
	
	def execute(self):
		self.RVector_out = self.RVector_in[self.route_ind]
		self.AvailPax_out = self.AvailPax_in[self.ac_ind]
		self.TurnAround = 1
		self.J = len(self.DVector[:,2]
		self.K = len(self.AvailPax_out)
		self.Lim = np.ones(self.K, self.J)
		
		self.Runway = 1e4 * len(self.RVector_out)
		self.MH_out = self.MH_in[self.ac_ind]
		self.FuelCost = 0.2431
		self.demfac = 1
		
class MaxTrip_3Route(Component):
	J = Int(iotype='in')
	K = Int(iotype='in')
	ACNum = Array(iotype='in')
	BlockTime = Array(iotype='in')
	MH = Array(iotype='in')
	TurnAround = Array(iotype='in')
	
	MaxTrip = Array(iotype='out')
	
	def execute(self):
		rw = 1
		max_trip = np.zeros(self.K*self.J)
		
		for kk in range(self.K):
			for jj in range(self.J):
				max_trip[rw] = self.ACNum[kk] * np.ceil(12/(self.BlockTime[kk, jj] * (1 + self.MH[kk]) + self.TurnAround))
				rw = rw + 1
				
		self.MaxTrip = max_trip

class MaxTrip_11Route(Component):
	J = Int(iotype='in')
	K = Int(iotype='in')
	ACNum = Array(iotype='in')
	BlockTime = Array(iotype='in')
	MH = Array(iotype='in')
	TurnAround = Array(iotype='in')
	
	MaxTrip = Array(iotype='out')
	
	def execute(self):
		rw = 1
		max_trip = np.zeros(self.K*self.J)
		
		for kk in range(self.K):
			for jj in range(self.J):
				max_trip[rw] = self.ACNum[kk] * np.ceil(12/(self.BlockTime[kk, jj] * (1 + self.MH[kk]) + self.TurnAround)) + 1
				rw = rw + 1
				
		self.MaxTrip = max_trip

class MaxTrip_31Route(Component):
	J = Int(iotype='in')
	K = Int(iotype='in')
	ACNum = Array(iotype='in')
	BlockTime = Array(iotype='in')
	MH = Array(iotype='in')
	TurnAround = Array(iotype='in')
	
	MaxTrip = Array(iotype='out')
	
	def execute(self):
		rw = 1
		max_trip = np.zeros(self.K*self.J)
		
		for kk in range(self.K):
			for jj in range(self.J):
				max_trip[rw] = self.ACNum[kk] * np.ceil(12/(self.BlockTime[kk, jj] * (1 + self.MH[kk]) + self.TurnAround))
				rw = rw + 1
				
		self.MaxTrip = max_trip
		
# Make sure that your class has some kind of docstring. Otherwise

# the descriptions for your variables won't show up in the

# source ducumentation.


class Airline_alloc(Component):

    """

    """

    # declare inputs and outputs here, for example:

    #x = Float(0.0, iotype='in', desc='description for x')

    #y = Float(0.0, iotype='out', desc='description for y')



    def execute(self):

        """ do your calculations here """

        pass

        