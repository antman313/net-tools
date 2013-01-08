from flask import Flask, json, render_template, request, Response

import netaddr


app = Flask('net-tools')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/networking/<subnet>/<mask>')
def subnet(subnet, mask):
    cidr = '{0}/{1}'.format(subnet, mask)
    ip = netaddr.IPNetwork(cidr)  # form.cidr.data)
    ips = list(ip)
    retval = {'network': str(ip.network),
              'broadcast': str(ip.broadcast),
              'net_size': str(ip.size),
              'range': '{0}-{1}'.format(ip[0], ip[-1])}
    js = json.dumps(retval)
    response = Response(js, status=200, mimetype='application/json')
    return response


if __name__ == '__main__':
    app.debug = True
    app.run()
