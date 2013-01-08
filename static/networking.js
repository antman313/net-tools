$(document).ready(function(){
    var SubnetModel = function() {
        self = this
        self.cidr =  ko.observable('')
        self.network =  ko.observable('')
        self.broadcast =  ko.observable('')
        self.net_size =  ko.observable('')
        self.range =  ko.observable('')
        self.process = function(){
            $.get('/networking/' + self.cidr(), function(data) {
              self.network(data.network)
              self.broadcast(data.broadcast)
              self.net_size(data.net_size)
              self.range(data.range)
            });
        }
    }
     
    ko.applyBindings(new SubnetModel())
});