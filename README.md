# DataSync Application

To Run the Application User need to enter database Username and Password

Prerequisites:

1. Create table company_data
2. Create table demo
 
Create Statements:

1.company_data:

CREATE TABLE `company_data` (
  `SrNo` int NOT NULL AUTO_INCREMENT,
  `BDM1Designation` varchar(250) DEFAULT NULL,
  `BDM2Designation` varchar(250) DEFAULT NULL,
  `BDM2EmailAddress1` varchar(250) DEFAULT NULL,
  `BDM2EmailAddress2` varchar(250) DEFAULT NULL,
  `BDM2PhoneNumber1` varchar(250) DEFAULT NULL,
  `BDM2PhoneNumber2` varchar(250) DEFAULT NULL,
  `BDMEmailAddress1` varchar(250) DEFAULT NULL,
  `BDMEmailAddress2` varchar(250) DEFAULT NULL,
  `BDMPhoneNumber1` varchar(250) DEFAULT NULL,
  `BDMPhoneNumber2` varchar(250) DEFAULT NULL,
  `BusinessDecisionMaker1` varchar(250) DEFAULT NULL,
  `BusinessDecisionMaker2` varchar(250) DEFAULT NULL,
  `CallStatus` varchar(250) DEFAULT NULL,
  `Comments` varchar(250) DEFAULT NULL,
  `CompanyName` varchar(250) DEFAULT NULL,
  `CRM` varchar(250) DEFAULT NULL,
  `DC` varchar(250) DEFAULT NULL,
  `DR` varchar(250) DEFAULT NULL,
  `ERP` varchar(250) DEFAULT NULL,
  `HeadquartersLocation` varchar(250) DEFAULT NULL,
  `ITBudgetSpendINRCrores` varchar(250) DEFAULT NULL,
  `ITDM2Designation` varchar(250) DEFAULT NULL,
  `ITDM2EmailAddress1` varchar(250) DEFAULT NULL,
  `ITDM2EmailAddress2` varchar(250) DEFAULT NULL,
  `ITDM2PhoneNumber1` varchar(250) DEFAULT NULL,
  `ITDM2PhoneNumber2` varchar(250) DEFAULT NULL,
  `ITDMDesignation` varchar(250) DEFAULT NULL,
  `ITDMEmailAddress1` varchar(250) DEFAULT NULL,
  `ITDMEmailAddress2` varchar(250) DEFAULT NULL,
  `ITDMPhoneNumber1` varchar(250) DEFAULT NULL,
  `ITDMPhoneNumber2` varchar(250) DEFAULT NULL,
  `Industry` varchar(250) DEFAULT NULL,
  `ITDecisionMaker1` varchar(250) DEFAULT NULL,
  `ITDecisionMaker2` varchar(250) DEFAULT NULL,
  `LinkedInProfile` varchar(250) DEFAULT NULL,
  `NewUpcomingProjects` varchar(250) DEFAULT NULL,
  `NumberOfEmployees` varchar(250) DEFAULT NULL,
  `NumberOfServers` varchar(250) DEFAULT NULL,
  `OperatingSystem` varchar(250) DEFAULT NULL,
  `Project` varchar(250) DEFAULT NULL,
  `ServersBrand` varchar(250) DEFAULT NULL,
  `SheetUsedBy` varchar(250) DEFAULT NULL,
  `StorageCapacity` varchar(250) DEFAULT NULL,
  `TurnoverINRCrores` varchar(250) DEFAULT NULL,
  `Website` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`SrNo`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


2.demo:
CREATE TABLE `demo` (
  `SrNo` int NOT NULL AUTO_INCREMENT,
  `BDM1Designation` varchar(250) DEFAULT NULL,
  `BDM2Designation` varchar(250) DEFAULT NULL,
  `BDM2EmailAddress1` varchar(250) DEFAULT NULL,
  `BDM2EmailAddress2` varchar(250) DEFAULT NULL,
  `BDM2PhoneNumber1` varchar(250) DEFAULT NULL,
  `BDM2PhoneNumber2` varchar(250) DEFAULT NULL,
  `BDMEmailAddress1` varchar(250) DEFAULT NULL,
  `BDMEmailAddress2` varchar(250) DEFAULT NULL,
  `BDMPhoneNumber1` varchar(250) DEFAULT NULL,
  `BDMPhoneNumber2` varchar(250) DEFAULT NULL,
  `BusinessDecisionMaker1` varchar(250) DEFAULT NULL,
  `BusinessDecisionMaker2` varchar(250) DEFAULT NULL,
  `CallStatus` varchar(250) DEFAULT NULL,
  `Comments` varchar(250) DEFAULT NULL,
  `CompanyName` varchar(250) DEFAULT NULL,
  `CRM` varchar(250) DEFAULT NULL,
  `DC` varchar(250) DEFAULT NULL,
  `DR` varchar(250) DEFAULT NULL,
  `ERP` varchar(250) DEFAULT NULL,
  `HeadquartersLocation` varchar(250) DEFAULT NULL,
  `ITBudgetSpendINRCrores` varchar(250) DEFAULT NULL,
  `ITDM2Designation` varchar(250) DEFAULT NULL,
  `ITDM2EmailAddress1` varchar(250) DEFAULT NULL,
  `ITDM2EmailAddress2` varchar(250) DEFAULT NULL,
  `ITDM2PhoneNumber1` varchar(250) DEFAULT NULL,
  `ITDM2PhoneNumber2` varchar(250) DEFAULT NULL,
  `ITDMDesignation` varchar(250) DEFAULT NULL,
  `ITDMEmailAddress1` varchar(250) DEFAULT NULL,
  `ITDMEmailAddress2` varchar(250) DEFAULT NULL,
  `ITDMPhoneNumber1` varchar(250) DEFAULT NULL,
  `ITDMPhoneNumber2` varchar(250) DEFAULT NULL,
  `Industry` varchar(250) DEFAULT NULL,
  `ITDecisionMaker1` varchar(250) DEFAULT NULL,
  `ITDecisionMaker2` varchar(250) DEFAULT NULL,
  `LinkedInProfile` varchar(250) DEFAULT NULL,
  `NewUpcomingProjects` varchar(250) DEFAULT NULL,
  `NumberOfEmployees` varchar(250) DEFAULT NULL,
  `NumberOfServers` varchar(250) DEFAULT NULL,
  `OperatingSystem` varchar(250) DEFAULT NULL,
  `Project` varchar(250) DEFAULT NULL,
  `ServersBrand` varchar(250) DEFAULT NULL,
  `SheetUsedBy` varchar(250) DEFAULT NULL,
  `StorageCapacity` varchar(250) DEFAULT NULL,
  `TurnoverINRCrores` varchar(250) DEFAULT NULL,
  `Website` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`SrNo`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
