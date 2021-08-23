
from lif import Lif
from nelif import Elif
from aelif import Aelif
from population import Population,draw_raster_plot
from Network import Network

#pop = Population().initialize_neurons().calculate_current()
a = Network()
a.initialize_populations().initialize_synapses().calculate_current()
#draw_raster_plot(pop)


