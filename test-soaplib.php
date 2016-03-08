<?php
$url = 'http://sdr.cs.colorado.edu:4444/php';
$soapclient = new SoapClient($url . '?wsdl', array(
						     'soap_version'       => SOAP_1_1,
						     'exceptions'         => true,
						     'features'           => SOAP_SINGLE_ELEMENT_ARRAYS,
						     ));

$getmetadataresult = $soapclient->getQuestionMetadata( "a", "b", "c" );
echo "meta info is ", $getmetadataresult;
?>
