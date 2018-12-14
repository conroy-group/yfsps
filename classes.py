


class SSPGen(object):

    def __init__(self):
        pass


class CSPGen(object):

    def __init__(self, wave, ssp_fluxes, ssp_grid):

        self.ssp_ages, self.ssp_feh, self.ssp_afe = ssp_grid
        self.wave = wave
        self.eline_wavelength = None
        self.ssp_fluxes = ssp_fluxes # Nssp x Nwave
        
        self.csp_params = {}

    def update(self, **kwargs):
        for k, v in kwargs.items():
            self.csp_params[k] = v

    def get_ssp_weights(self, sfh_params):
        # do stuff
        return total_weights

    def construct_spectrum(self):

        weights = self.get_ssp_weights()                               # Nssp
        lines, cont = self.add_neb()                                   # Nssp x Nline, Nssp x Nwave
        
        # Attenuation
        attenuation = np.exp(-self.dust_attenuation(self.wave))        # Nssp x Nwave
        line_attenuation = np.exp(-self.dust_attenuation(self.eline_wavelengths)) # Nssp * Nline

        # Combine SSps with attenuation
        spec = np.dot(weights, self.ssp_fluxes * attenuation)          # Nwave
        line = np.dot(weights, lines * line_attenuation)

        # Calculate absorbed light
        absorbed = self.dust_absorb(weights, ssp_fluxes, attenuation)  # scalar
        line_abs  = self.dust_absorb(weights, lines, line_attenuation)

        # add dust emission
        spec += (absorbed + line_abs) * self.dust_sed()       
        
        return spec


    def dust_attenuation(self, wavelengths):
        # do stuff.  Could take a "dust model" object.
        return attenuation_curves * optical depths

    def dust_absorb(self):
        # idk, some iterative convergent thing?
        absorbed = self.trapz(np.dot(weights, ssp_flux * (1-dust)), self.wave)
        return absorbed

    def dust_sed(self):
        # draine & li
        pass

    def add_neb(self):
        # interpolate cloudyfsps tables
        return emission_lines, nebular_continuua


def igm_attenuate(zred, wave, spec):
    #class, needs to interpolate tables
    pass

def add_agn(tau_agn, fagn, wave, spec):
    # class, needs to interpolate tables
    pass

def smooth(wave, spec, smoothparameters):
    # copy from prospector smoothspec
    pass

def get_mags(zred, wave, spec, filters):
    # copy from sedpy
    pass
