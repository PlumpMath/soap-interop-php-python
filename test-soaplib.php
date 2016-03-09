<?php

if ( 1 ) {

  $url = 'http://sdr.cs.colorado.edu:4444/php';
  $soapclient = new SoapClient($url . '?wsdl', array(
						     'soap_version'       => SOAP_1_1,
						     'exceptions'         => true,
						     'features'           => SOAP_SINGLE_ELEMENT_ARRAYS,
						     ));

  $getmetadataresult = $soapclient->getQuestionMetadata( "a", "b", "c" );
  echo "meta info is ", $getmetadataresult;
 } else {
  /* alternate test using Spyne say_hello  code -- also fails with soaplib */

  $url = 'http://localhost:8000/php';
  $soapclient = new SoapClient($url . '?wsdl', array(
						     'soap_version'       => SOAP_1_1,
						     'exceptions'         => true,
						     'features'           => SOAP_SINGLE_ELEMENT_ARRAYS,
						     ));

  $getmetadataresult = $soapclient->say_hello( "foo", "a", 3);
  echo "meta info is ", $getmetadataresult;
 }
?>
