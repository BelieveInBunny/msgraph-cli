# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class Microsoftgraphactionstate(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    PENDING = "pending"
    CANCELED = "canceled"
    ACTIVE = "active"
    DONE = "done"
    FAILED = "failed"
    NOTSUPPORTED = "notSupported"

class Microsoftgraphactivitydomain(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    UNKNOWN = "unknown"
    WORK = "work"
    PERSONAL = "personal"
    UNRESTRICTED = "unrestricted"

class Microsoftgraphattachmenttype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    FILE = "file"
    ITEM = "item"
    REFERENCE = "reference"

class Microsoftgraphattendeetype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    REQUIRED = "required"
    OPTIONAL = "optional"
    RESOURCE = "resource"

class Microsoftgraphautomaticrepliesstatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    DISABLED = "disabled"
    ALWAYSENABLED = "alwaysEnabled"
    SCHEDULED = "scheduled"

class Microsoftgraphbodytype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    TEXT = "text"
    HTML = "html"

class Microsoftgraphcalendarcolor(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    LIGHTBLUE = "lightBlue"
    LIGHTGREEN = "lightGreen"
    AUTO = "auto"
    LIGHTORANGE = "lightOrange"
    LIGHTGRAY = "lightGray"
    LIGHTYELLOW = "lightYellow"
    LIGHTTEAL = "lightTeal"
    LIGHTPINK = "lightPink"
    LIGHTBROWN = "lightBrown"
    LIGHTRED = "lightRed"
    MAXCOLOR = "maxColor"

class Microsoftgraphcalendarroletype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    FREEBUSYREAD = "freeBusyRead"
    LIMITEDREAD = "limitedRead"
    READ = "read"
    WRITE = "write"
    DELEGATEWITHOUTPRIVATEEVENTACCESS = "delegateWithoutPrivateEventAccess"
    DELEGATEWITHPRIVATEEVENTACCESS = "delegateWithPrivateEventAccess"
    CUSTOM = "custom"

class Microsoftgraphcategorycolor(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    PRESET0 = "preset0"
    PRESET1 = "preset1"
    NONE = "none"
    PRESET2 = "preset2"
    PRESET3 = "preset3"
    PRESET4 = "preset4"
    PRESET5 = "preset5"
    PRESET6 = "preset6"
    PRESET7 = "preset7"
    PRESET8 = "preset8"
    PRESET9 = "preset9"
    PRESET10 = "preset10"
    PRESET11 = "preset11"
    PRESET12 = "preset12"
    PRESET13 = "preset13"
    PRESET14 = "preset14"
    PRESET15 = "preset15"
    PRESET16 = "preset16"
    PRESET17 = "preset17"
    PRESET18 = "preset18"
    PRESET19 = "preset19"
    PRESET20 = "preset20"
    PRESET21 = "preset21"
    PRESET22 = "preset22"
    PRESET23 = "preset23"
    PRESET24 = "preset24"

class Microsoftgraphchannelmembershiptype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    STANDARD = "standard"
    PRIVATE = "private"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphchatmessageimportance(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NORMAL = "normal"
    HIGH = "high"
    URGENT = "urgent"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphchatmessagepolicyviolationdlpactiontypes(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    NOTIFYSENDER = "notifySender"
    BLOCKACCESS = "blockAccess"
    BLOCKACCESSEXTERNAL = "blockAccessExternal"

class Microsoftgraphchatmessagepolicyviolationuseractiontypes(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    OVERRIDE = "override"
    REPORTFALSEPOSITIVE = "reportFalsePositive"

class Microsoftgraphchatmessagepolicyviolationverdictdetailstypes(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    ALLOWFALSEPOSITIVEOVERRIDE = "allowFalsePositiveOverride"
    ALLOWOVERRIDEWITHOUTJUSTIFICATION = "allowOverrideWithoutJustification"
    ALLOWOVERRIDEWITHJUSTIFICATION = "allowOverrideWithJustification"

class Microsoftgraphchatmessagetype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    MESSAGE = "message"
    CHATEVENT = "chatEvent"
    TYPING = "typing"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphcompliancestate(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    UNKNOWN = "unknown"
    COMPLIANT = "compliant"
    NONCOMPLIANT = "noncompliant"
    CONFLICT = "conflict"
    ERROR = "error"
    INGRACEPERIOD = "inGracePeriod"
    CONFIGMANAGER = "configManager"

class Microsoftgraphcompliancestatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    UNKNOWN = "unknown"
    NOTAPPLICABLE = "notApplicable"
    COMPLIANT = "compliant"
    REMEDIATED = "remediated"
    NONCOMPLIANT = "nonCompliant"
    ERROR = "error"
    CONFLICT = "conflict"
    NOTASSIGNED = "notAssigned"

class Microsoftgraphdayofweek(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    SUNDAY = "sunday"
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"

class Microsoftgraphdelegatemeetingmessagedeliveryoptions(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    SENDTODELEGATEANDINFORMATIONTOPRINCIPAL = "sendToDelegateAndInformationToPrincipal"
    SENDTODELEGATEANDPRINCIPAL = "sendToDelegateAndPrincipal"
    SENDTODELEGATEONLY = "sendToDelegateOnly"

class Microsoftgraphdeviceenrollmenttype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    UNKNOWN = "unknown"
    USERENROLLMENT = "userEnrollment"
    DEVICEENROLLMENTMANAGER = "deviceEnrollmentManager"
    APPLEBULKWITHUSER = "appleBulkWithUser"
    APPLEBULKWITHOUTUSER = "appleBulkWithoutUser"
    WINDOWSAZUREADJOIN = "windowsAzureADJoin"
    WINDOWSBULKUSERLESS = "windowsBulkUserless"
    WINDOWSAUTOENROLLMENT = "windowsAutoEnrollment"
    WINDOWSBULKAZUREDOMAINJOIN = "windowsBulkAzureDomainJoin"
    WINDOWSCOMANAGEMENT = "windowsCoManagement"

class Microsoftgraphdevicemanagementexchangeaccessstate(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    UNKNOWN = "unknown"
    ALLOWED = "allowed"
    BLOCKED = "blocked"
    QUARANTINED = "quarantined"

class Microsoftgraphdevicemanagementexchangeaccessstatereason(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    UNKNOWN = "unknown"
    EXCHANGEGLOBALRULE = "exchangeGlobalRule"
    EXCHANGEINDIVIDUALRULE = "exchangeIndividualRule"
    EXCHANGEDEVICERULE = "exchangeDeviceRule"
    EXCHANGEUPGRADE = "exchangeUpgrade"
    EXCHANGEMAILBOXPOLICY = "exchangeMailboxPolicy"
    OTHER = "other"
    COMPLIANT = "compliant"
    NOTCOMPLIANT = "notCompliant"
    NOTENROLLED = "notEnrolled"
    UNKNOWNLOCATION = "unknownLocation"
    MFAREQUIRED = "mfaRequired"
    AZUREADBLOCKDUETOACCESSPOLICY = "azureADBlockDueToAccessPolicy"
    COMPROMISEDPASSWORD = "compromisedPassword"
    DEVICENOTKNOWNWITHMANAGEDAPP = "deviceNotKnownWithManagedApp"

class Microsoftgraphdeviceregistrationstate(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOTREGISTERED = "notRegistered"
    REGISTERED = "registered"
    REVOKED = "revoked"
    KEYCONFLICT = "keyConflict"
    APPROVALPENDING = "approvalPending"
    CERTIFICATERESET = "certificateReset"
    NOTREGISTEREDPENDINGENROLLMENT = "notRegisteredPendingEnrollment"
    UNKNOWN = "unknown"

class Microsoftgrapheventtype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    SINGLEINSTANCE = "singleInstance"
    OCCURRENCE = "occurrence"
    EXCEPTION = "exception"
    SERIESMASTER = "seriesMaster"

class Microsoftgraphexchangeidformat(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ENTRYID = "entryId"
    EWSID = "ewsId"
    IMMUTABLEENTRYID = "immutableEntryId"
    RESTID = "restId"
    RESTIMMUTABLEENTRYID = "restImmutableEntryId"

class Microsoftgraphexternalaudiencescope(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    CONTACTSONLY = "contactsOnly"
    ALL = "all"

class Microsoftgraphfollowupflagstatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOTFLAGGED = "notFlagged"
    COMPLETE = "complete"
    FLAGGED = "flagged"

class Microsoftgraphfreebusystatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    FREE = "free"
    TENTATIVE = "tentative"
    UNKNOWN = "unknown"
    BUSY = "busy"
    OOF = "oof"
    WORKINGELSEWHERE = "workingElsewhere"

class Microsoftgraphgiphyratingtype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    STRICT = "strict"
    MODERATE = "moderate"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphimportance(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"

class Microsoftgraphinferenceclassificationtype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    FOCUSED = "focused"
    OTHER = "other"

class Microsoftgraphlocationtype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    DEFAULT = "default"
    CONFERENCEROOM = "conferenceRoom"
    HOMEADDRESS = "homeAddress"
    BUSINESSADDRESS = "businessAddress"
    GEOCOORDINATES = "geoCoordinates"
    STREETADDRESS = "streetAddress"
    HOTEL = "hotel"
    RESTAURANT = "restaurant"
    LOCALBUSINESS = "localBusiness"
    POSTALADDRESS = "postalAddress"

class Microsoftgraphlocationuniqueidtype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    UNKNOWN = "unknown"
    LOCATIONSTORE = "locationStore"
    DIRECTORY = "directory"
    PRIVATE = "private"
    BING = "bing"

class Microsoftgraphmailtipstype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    AUTOMATICREPLIES = "automaticReplies"
    MAILBOXFULLSTATUS = "mailboxFullStatus"
    CUSTOMMAILTIP = "customMailTip"
    EXTERNALMEMBERCOUNT = "externalMemberCount"
    TOTALMEMBERCOUNT = "totalMemberCount"
    MAXMESSAGESIZE = "maxMessageSize"
    DELIVERYRESTRICTION = "deliveryRestriction"
    MODERATIONSTATUS = "moderationStatus"
    RECIPIENTSCOPE = "recipientScope"
    RECIPIENTSUGGESTIONS = "recipientSuggestions"

class Microsoftgraphmanagedappflaggedreason(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    ROOTEDDEVICE = "rootedDevice"

class Microsoftgraphmanageddeviceownertype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    UNKNOWN = "unknown"
    COMPANY = "company"
    PERSONAL = "personal"

class Microsoftgraphmanageddevicepartnerreportedhealthstate(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    UNKNOWN = "unknown"
    ACTIVATED = "activated"
    DEACTIVATED = "deactivated"
    SECURED = "secured"
    LOWSEVERITY = "lowSeverity"
    MEDIUMSEVERITY = "mediumSeverity"
    HIGHSEVERITY = "highSeverity"
    UNRESPONSIVE = "unresponsive"
    COMPROMISED = "compromised"
    MISCONFIGURED = "misconfigured"

class Microsoftgraphmanagementagenttype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    EAS = "eas"
    MDM = "mdm"
    EASMDM = "easMdm"
    INTUNECLIENT = "intuneClient"
    EASINTUNECLIENT = "easIntuneClient"
    CONFIGURATIONMANAGERCLIENT = "configurationManagerClient"
    CONFIGURATIONMANAGERCLIENTMDM = "configurationManagerClientMdm"
    CONFIGURATIONMANAGERCLIENTMDMEAS = "configurationManagerClientMdmEas"
    UNKNOWN = "unknown"
    JAMF = "jamf"
    GOOGLECLOUDDEVICEPOLICYCONTROLLER = "googleCloudDevicePolicyController"

class Microsoftgraphmessageactionflag(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ANY = "any"
    CALL = "call"
    DONOTFORWARD = "doNotForward"
    FOLLOWUP = "followUp"
    FYI = "fyi"
    FORWARD = "forward"
    NORESPONSENECESSARY = "noResponseNecessary"
    READ = "read"
    REPLY = "reply"
    REPLYTOALL = "replyToAll"
    REVIEW = "review"

class Microsoftgraphonenotepatchactiontype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    REPLACE = "Replace"
    APPEND = "Append"
    DELETE = "Delete"
    INSERT = "Insert"
    PREPEND = "Prepend"

class Microsoftgraphonenotepatchinsertposition(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    AFTER = "After"
    BEFORE = "Before"

class Microsoftgraphonenoteuserrole(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    OWNER = "Owner"
    CONTRIBUTOR = "Contributor"
    NONE = "None"
    READER = "Reader"

class Microsoftgraphonlinemeetingprovidertype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    UNKNOWN = "unknown"
    SKYPEFORBUSINESS = "skypeForBusiness"
    SKYPEFORCONSUMER = "skypeForConsumer"
    TEAMSFORBUSINESS = "teamsForBusiness"

class Microsoftgraphoperationstatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOTSTARTED = "NotStarted"
    RUNNING = "Running"
    COMPLETED = "Completed"
    FAILED = "Failed"

class Microsoftgraphphonetype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    HOME = "home"
    BUSINESS = "business"
    MOBILE = "mobile"
    OTHER = "other"
    ASSISTANT = "assistant"
    HOMEFAX = "homeFax"
    BUSINESSFAX = "businessFax"
    OTHERFAX = "otherFax"
    PAGER = "pager"
    RADIO = "radio"

class Microsoftgraphplannerpreviewtype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    AUTOMATIC = "automatic"
    NOPREVIEW = "noPreview"
    CHECKLIST = "checklist"
    DESCRIPTION = "description"
    REFERENCE = "reference"

class Microsoftgraphpolicyplatformtype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ANDROID = "android"
    IOS = "iOS"
    MACOS = "macOS"
    WINDOWSPHONE81 = "windowsPhone81"
    WINDOWS81ANDLATER = "windows81AndLater"
    WINDOWS10ANDLATER = "windows10AndLater"
    ANDROIDWORKPROFILE = "androidWorkProfile"
    ALL = "all"

class Microsoftgraphrecipientscopetype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    INTERNAL = "internal"
    EXTERNAL = "external"
    EXTERNALPARTNER = "externalPartner"
    EXTERNALNONPARTNER = "externalNonPartner"

class Microsoftgraphrecurrencepatterntype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    DAILY = "daily"
    WEEKLY = "weekly"
    ABSOLUTEMONTHLY = "absoluteMonthly"
    RELATIVEMONTHLY = "relativeMonthly"
    ABSOLUTEYEARLY = "absoluteYearly"
    RELATIVEYEARLY = "relativeYearly"

class Microsoftgraphrecurrencerangetype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ENDDATE = "endDate"
    NOEND = "noEnd"
    NUMBERED = "numbered"

class Microsoftgraphresponsetype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    ORGANIZER = "organizer"
    TENTATIVELYACCEPTED = "tentativelyAccepted"
    ACCEPTED = "accepted"
    DECLINED = "declined"
    NOTRESPONDED = "notResponded"

class Microsoftgraphschedulechangerequestactor(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    SENDER = "sender"
    RECIPIENT = "recipient"
    MANAGER = "manager"
    SYSTEM = "system"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphschedulechangestate(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    PENDING = "pending"
    APPROVED = "approved"
    DECLINED = "declined"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphscheduleentitytheme(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    WHITE = "white"
    BLUE = "blue"
    GREEN = "green"
    PURPLE = "purple"
    PINK = "pink"
    YELLOW = "yellow"
    GRAY = "gray"
    DARKBLUE = "darkBlue"
    DARKGREEN = "darkGreen"
    DARKPURPLE = "darkPurple"
    DARKPINK = "darkPink"
    DARKYELLOW = "darkYellow"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphselectionlikelihoodinfo(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOTSPECIFIED = "notSpecified"
    HIGH = "high"

class Microsoftgraphsensitivity(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NORMAL = "normal"
    PERSONAL = "personal"
    PRIVATE = "private"
    CONFIDENTIAL = "confidential"

class Microsoftgraphstatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ACTIVE = "active"
    UPDATED = "updated"
    DELETED = "deleted"
    IGNORED = "ignored"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphteamsappdistributionmethod(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    STORE = "store"
    ORGANIZATION = "organization"
    SIDELOADED = "sideloaded"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphteamsasyncoperationstatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    INVALID = "invalid"
    NOTSTARTED = "notStarted"
    INPROGRESS = "inProgress"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphteamsasyncoperationtype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    INVALID = "invalid"
    CLONETEAM = "cloneTeam"
    ARCHIVETEAM = "archiveTeam"
    UNARCHIVETEAM = "unarchiveTeam"
    CREATETEAM = "createTeam"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphteamspecialization(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    EDUCATIONSTANDARD = "educationStandard"
    EDUCATIONCLASS = "educationClass"
    EDUCATIONPROFESSIONALLEARNINGCOMMUNITY = "educationProfessionalLearningCommunity"
    EDUCATIONSTAFF = "educationStaff"
    HEALTHCARESTANDARD = "healthcareStandard"
    HEALTHCARECARECOORDINATION = "healthcareCareCoordination"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphteamvisibilitytype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    PRIVATE = "private"
    PUBLIC = "public"
    HIDDENMEMBERSHIP = "hiddenMembership"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphtimeoffreasonicontype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NONE = "none"
    CAR = "car"
    CALENDAR = "calendar"
    RUNNING = "running"
    PLANE = "plane"
    FIRSTAID = "firstAid"
    DOCTOR = "doctor"
    NOTWORKING = "notWorking"
    CLOCK = "clock"
    JURYDUTY = "juryDuty"
    GLOBE = "globe"
    CUP = "cup"
    PHONE = "phone"
    WEATHER = "weather"
    UMBRELLA = "umbrella"
    PIGGYBANK = "piggyBank"
    DOG = "dog"
    CAKE = "cake"
    TRAFFICCONE = "trafficCone"
    PIN = "pin"
    SUNNY = "sunny"
    UNKNOWNFUTUREVALUE = "unknownFutureValue"

class Microsoftgraphwebsitetype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    OTHER = "other"
    HOME = "home"
    WORK = "work"
    BLOG = "blog"
    PROFILE = "profile"

class Microsoftgraphweekindex(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    FIRST = "first"
    SECOND = "second"
    THIRD = "third"
    FOURTH = "fourth"
    LAST = "last"

class Microsoftgraphworkbookoperationstatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOTSTARTED = "notStarted"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
