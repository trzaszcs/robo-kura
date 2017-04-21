from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer
from pybrain.datasets import UnsupervisedDataSet
 
class NetworkHelper(object):
     
    # create dataset
    def create_dataset(self):
         
        dataset = SupervisedDataSet(2,1)
 
        dataset.addSample([1,1],[0])
        dataset.addSample([1,0],[1])
        dataset.addSample([0,1],[1])
        dataset.addSample([0,0],[0])
 
        return dataset
 
    # create network
    def create_network(self, dataset):
 
        return buildNetwork(dataset.indim, 3, dataset.outdim, recurrent=True)
 
    # train network on supplied dataset
    def train_network(self, network, dataset):
 
        trainer = BackpropTrainer(network, dataset, learningrate = 0.01, momentum = 0.99, verbose = True)
        for epoch in range(0, 1000):
            trainer.train()
         
        return network
 
    # test network on supplied data
    def test_network(self, network, data):
 
        dataset = UnsupervisedDataSet(2)
        dataset.addSample(data)  
         
        return network.activateOnDataset(dataset)[0]

