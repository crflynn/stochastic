import os
import random

import matplotlib.pyplot as plt

from stochastic.processes import *

plt.style.use("bmh")


def make_plot(
    title, fname, x, ys, xlabel="Time", ylabel="Value", scatter=False, alt=False
):
    fig, ax = plt.subplots(1, 1, figsize=(8, 4))
    if alt:
        for y in ys:
            if scatter:
                ax.scatter(y, range(len(y)))
            else:
                ax.plot(y, range(len(y)))
    else:
        for y in ys:
            if scatter:
                ax.scatter(x, y)
            else:
                ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    # ax.axes.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig(os.path.join((os.path.dirname(__file__)), "_static", f"{fname}.png"))
    print(title + " saved")
    plt.close()


def get_samples(num, inst, args):
    ss = []
    for k in range(num):
        ss.append(inst.sample(**args))
    return ss


def main():
    # # Continuous
    # dim = 3
    # n_samples = 3
    # n = 2 ** 12
    # process = BesselProcess(t=1, dim=dim)
    # t = process.times(n)
    #
    # ss = get_samples(n_samples, process, {"n": n})
    # make_plot("Bessel process (dim=3)", "bessel_process", t, ss, "Time", "Value")
    #
    # process = BrownianBridge(t=1, b=0)
    # ss = get_samples(n_samples, process, {"n": n})
    # make_plot("Brownian bridge (b=0)", "brownian_bridge", t, ss, "Time", "Value")
    #
    # process = BrownianExcursion(t=1)
    # ss = get_samples(n_samples, process, {"n": n})
    # make_plot("Brownian excursion", "brownian_excursion", t, ss, "Time", "Value")
    #
    # process = BrownianMeander(t=1)
    # ss = get_samples(n_samples, process, {"n": n})
    # make_plot("Brownian meander", "brownian_meander", t, ss, "Time", "Value")
    #
    # process = BrownianMotion(t=1)
    # ss = get_samples(n_samples, process, {"n": n})
    # make_plot("Brownian motion", "brownian_motion", t, ss, "Time", "Value")
    #
    # process = CauchyProcess(t=1)
    # ss = get_samples(n_samples, process, {"n": n})
    # make_plot("Cauchy process", "cauchy_process", t, ss, "Time", "Value")
    #
    # process = FractionalBrownianMotion(t=1, hurst = 0.7)
    # ss = get_samples(n_samples, process, {"n": n})
    # make_plot("Fractional Brownian motion (hurst=0.7)", "fractional_brownian_motion", t, ss, "Time", "Value")
    #
    # process = GammaProcess(t=1, mean=1, variance=1)
    # ss = get_samples(n_samples, process, {"n": n})
    # make_plot("Gamma process (mean=1, variance=1)", "gamma_process", t, ss, "Time", "Value")
    #
    # process = GeometricBrownianMotion(t=1)
    # ss = get_samples(n_samples, process, {"n": n, "initial": 1})
    # make_plot("Geometric Brownian motion (drift=0, volatility=1)", "geometric_brownian_motion", t, ss, "Time", "Value")
    #
    # process = PoissonProcess(rate=1)
    # ss = get_samples(n_samples, process, {"n": 500})
    # make_plot("Poisson process (rate=1)", "poisson_process", t, ss, "Time", "Value", alt=True)
    #
    # process = SquaredBesselProcess(t=1, dim=3)
    # ss = get_samples(n_samples, process, {"n": n})
    # make_plot("Squared Bessel process (dim=3)", "squared_bessel_process", t, ss, "Time", "Value")
    #
    # process = VarianceGammaProcess(t=1, drift=0, variance=1, scale=1)
    # ss = get_samples(n_samples, process, {"n": n})
    # make_plot("Variance Gamma process (drift=0, variance=1, scale=1)", "variance_gamma_process", t, ss, "Time", "Value")
    #
    # process = WienerProcess(t=1)
    # ss = get_samples(n_samples, process, {"n": n})
    # make_plot("Wiener process", "wiener_process", t, ss, "Time", "Value")
    #
    # process = ConstantElasticityVarianceProcess(t=1)
    # ss = get_samples(n_samples, process, {"n": n})
    # make_plot("CEV process", "constant_elasticity_variance_process", t, ss, "Time", "Value")
    #
    # process = CoxIngersollRossProcess(t=1)
    # ss = get_samples(n_samples, process, {"n": n})
    # make_plot("CIR process", "cox_ingersoll_ross_process", t, ss, "Time", "Value")
    #
    # process = OrnsteinUhlenbeckProcess(t=1)
    # ss = get_samples(n_samples, process, {"n": n})
    # make_plot("Ornstein-Uhlenbeck process", "ornstein_uhlenbeck_process", t, ss, "Time", "Value")
    #
    # process = VasicekProcess(t=1)
    # ss = get_samples(n_samples, process, {"n": n})
    # make_plot("Vasicek process", "vasicek_process", t, ss, "Time", "Value")
    #
    # process = BernoulliProcess(p=0.5)
    # ss = get_samples(1, process, {"n": 16})
    # make_plot("Bernoulli process", "bernoulli_process", list(range(16)), ss, "Time", "Value", scatter=True)
    #
    # process = ChineseRestaurantProcess()
    # ss = get_samples(1, process, {"n": 64})
    # make_plot("Chinese Restaurant process", "chinese_restaurant_process", list(range(64)), ss, "Time", "Value", scatter=True)
    #
    process = DirichletProcess()
    ss = get_samples(1, process, {"n": 64})
    make_plot(
        "Dirichlet process",
        "dirichlet_process",
        list(range(64)),
        ss,
        "Time",
        "Value",
        scatter=True,
    )

    # process = MarkovChain([[0.2, 0.2, 0.2, 0.2, 0.2],[0.2, 0.2, 0.2, 0.2, 0.2],[0.2, 0.2, 0.2, 0.2, 0.2],[0.2, 0.2, 0.2, 0.2, 0.2],[0.2, 0.2, 0.2, 0.2, 0.2]])
    # ss = get_samples(1, process, {"n": 32})
    # make_plot("Markov chain (5 states)", "markov_chain", list(range(32)), ss, "Time", "Value", scatter=True)
    #
    # process = MoranProcess(maximum=20)
    # ss = get_samples(n_samples, process, {"n": 50, "start": 10})
    # make_plot("Moran process", "moran_process", list(range(50)), ss, "Time", "Value", scatter=True)
    #
    # process = RandomWalk()
    # ss = get_samples(n_samples, process, {"n": 64})
    # make_plot("Random walk", "random_walk", list(range(64+1)), ss, "Time", "Value", scatter=True)
    #
    # process = FractionalGaussianNoise(t=1, hurst=0.2)
    # ss = get_samples(1, process, {"n": 2**8})
    # for idx, s in enumerate(ss):
    #     ss[idx] = np.insert(s, 0, [0])
    # make_plot("Fractional Gaussian noise (hurst=0.2)", "fractional_gaussian_noise", process.times(2**8), ss, "Time", "Value")
    #
    # process = GaussianNoise(t=1)
    # ss = get_samples(1, process, {"n": 2**8})
    # for idx, s in enumerate(ss):
    #     ss[idx] = np.insert(s, 0, [0])
    # make_plot("Gaussian noise", "gaussian_noise", process.times(2**8), ss, "Time", "Value")
    #
    # colors = {
    #     "White": 0,
    #     "Pink": 1,
    #     "Red": 2,
    # }
    # ys = []
    # for color, beta in colors.items():
    #     process = ColoredNoise(beta)
    #     ys.append(process.sample(n))
    #     t = process.times(n)
    # make_plot("Colored noise", "colored_noise", t, ys, "Time", "Value")
    #
    # colors = {
    #     "Violet": -2,
    #     "Blue": -1,
    #     "White": 0,
    #     "Pink": 1,
    #     "Red": 2,
    # }
    # for color, beta in colors.items():
    #     process = ColoredNoise(beta)
    #     ys = []
    #     ys.append(process.sample(n))
    #     t = process.times(n)
    #     make_plot("{c} noise".format(c=color), "{c}_noise".format(c=color.lower()), t, ys, "Time", "Value")
    #
    # def h(t):
    #     return math.sin(t*4*math.pi) * 0.4 + 0.5
    # process = MultifractionalBrownianMotion(t=1, hurst=h)
    # t = process.times(n)
    # ss = get_samples(n_samples, process, {"n": n})
    #
    # make_plot("Multifractional Brownian motion", "multifractional_brownian_motion", t, ss)
    #
    # process = InverseGaussianProcess()
    # t = process.times(n)
    # ss = get_samples(n_samples, process, {"n": n})
    #
    # make_plot("Inverse Gaussian process", "inverse_gaussian", t, ss)
    #
    # process = MixedPoissonProcess(random.uniform, (1, 5))
    # ss = get_samples(n_samples, process, {"n": 500})
    # make_plot(
    #     "Mixed Poisson process", "mixed_poisson_process", t, ss, "Time", "Value", alt=True,
    # )


if __name__ == "__main__":
    main()
