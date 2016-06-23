Azion-nf
========
Registry Tool and search for invoices.

*Azion-nf was developed to register what the customers buy, according with the services that the company provides.
The interface is an easy channel to access to the relation of clients, services and invoices through an simple interface and also the Django admin interface. One of the tools is the option to export the Invoice to a PDF format and save to the local disk.*

## Table of contents

 1. [Requisites](#requisites)
 1. [Running](#running)
 1. [Static](#static)
 1. [Pushing Code](#pushing-code)
 1. [Functionality](#functionality)


## Requisites

Azion-nf uses [vagrant](http://www.vagrantup.com/) as an environment to easily develop and build the project.
Download and install Vagrant.

After installing Vagrant, issue the following commands:

    git clone https://github.com/aziontech/azion-nf/.git
    git fetch && git checkout dev

Now, you can start your Vagrant:

    vagrant up
    vagrant ssh

On a fresh installation, Vagrant will also install all system packages, to do that again the future run:

    vagrant reload --provision

You will need a virtualenv to install all **python** packages.
To achieve this you can use virtualenv or virtualenvwrapper (virtualenvwrapper is prefered):

For **virtualenvwrapper**:

    mkvirtualenv temp

Or for **virtualenv** only:

    virtualenv env
    source env/bin/activate

After installing and activating virtualenv you are able to install all the packages:

    pip install -r requirements.txt

Install Phantomjs to use the functionality of PDF generate of invoices:

    yum-based systems:

    sudo yum install gcc gcc-c++ make git openssl-devel freetype-devel fontconfig-devel
    git clone git://github.com/ariya/phantomjs.git
    cd phantomjs
    git checkout 1.9
    ./build.sh

    yum install xorg-x11-fonts-Type1

## Running

After all packages installed, you can create the database running:

    python manage.py syncdb

Run the system with the command:

	python manage.py runserver 0.0.0.0:8080

First of all access the Django Admin Interface and register at least one Client and One Service to start register Invoices.

You can Access the Django Admin Interface on the following link:

	http://127.0.0.1:8080/admin

You can access the Azion-nf System interface on the following address:

	http://127.0.0.1:8080/

## Static
	
One of the requirements for this project is the Django Widgets Tweaks that is a tool for management of the CSS class of the System Template. So, to each new template file use the " {% load widget_tweaks %} " tag on the top of yout HTML code.


## Pushing Code

To contribute with the project, you need to work with pull requests.
All pull requests are analyzed and merged within dev branch.

There is a list of issues [here](https://github.com/aziontech/azion-nf/issues?state=open)

To create a branch from the **dev** branch:

    git checkout dev
    git pull origin dev
    git branch your_new_branch

Commit any changes in your new branch, push it to Github and submit a pull request [here](https://github.com/aziontech/azion-nf/compare/)

## Functionality

The Azion NF system was developed to register Client data, Services provided by the company, and the Invoices of each customer buy.

The First screen shows the list of the clients and links to other pages to register a new invoice, or view a history of the invoices listed by client.

These options can be accessed by the buttons "Gerar NF" and "Historico de NF".

At the Invoice Register Screen (Gerar NF) the client data will be auto loaded and its possible chose the services and fill the prices of each one.

The button "Gravar" will save this Invoice with the services, client data, date and a register number. 

The button "Gravar e enviar por e-mail" will save this invoice and redirect to a link with the Invoice PDF File to send by e-mail.

At the Invoice History Screen (Historico de NF) are listed the invoices registered for the selected client, listed by date.


















