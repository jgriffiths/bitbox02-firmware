#[derive(Clone, PartialEq, ::prost::Message)]
pub struct PubResponse {
    #[prost(string, tag="1")]
    pub r#pub: ::prost::alloc::string::String,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RootFingerprintRequest {
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RootFingerprintResponse {
    #[prost(bytes, tag="1")]
    pub fingerprint: ::prost::alloc::vec::Vec<u8>,
}
/// See https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki.
/// version field dropped as it will set dynamically based on the context (xpub, ypub, etc.).
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct XPub {
    #[prost(bytes, tag="1")]
    pub depth: ::prost::alloc::vec::Vec<u8>,
    #[prost(bytes, tag="2")]
    pub parent_fingerprint: ::prost::alloc::vec::Vec<u8>,
    #[prost(uint32, tag="3")]
    pub child_num: u32,
    #[prost(bytes, tag="4")]
    pub chain_code: ::prost::alloc::vec::Vec<u8>,
    #[prost(bytes, tag="5")]
    pub public_key: ::prost::alloc::vec::Vec<u8>,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct CheckBackupRequest {
    #[prost(bool, tag="1")]
    pub silent: bool,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct CheckBackupResponse {
    #[prost(string, tag="1")]
    pub id: ::prost::alloc::string::String,
}
/// Timestamp must be in UTC
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct CreateBackupRequest {
    #[prost(uint32, tag="1")]
    pub timestamp: u32,
    #[prost(int32, tag="2")]
    pub timezone_offset: i32,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ListBackupsRequest {
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BackupInfo {
    #[prost(string, tag="1")]
    pub id: ::prost::alloc::string::String,
    #[prost(uint32, tag="2")]
    pub timestamp: u32,
    /// uint32 timezone_offset = 3;
    #[prost(string, tag="4")]
    pub name: ::prost::alloc::string::String,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ListBackupsResponse {
    #[prost(message, repeated, tag="1")]
    pub info: ::prost::alloc::vec::Vec<BackupInfo>,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RestoreBackupRequest {
    #[prost(string, tag="1")]
    pub id: ::prost::alloc::string::String,
    #[prost(uint32, tag="2")]
    pub timestamp: u32,
    #[prost(int32, tag="3")]
    pub timezone_offset: i32,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct CheckSdCardRequest {
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct CheckSdCardResponse {
    #[prost(bool, tag="1")]
    pub inserted: bool,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct DeviceInfoRequest {
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct DeviceInfoResponse {
    #[prost(string, tag="1")]
    pub name: ::prost::alloc::string::String,
    #[prost(bool, tag="2")]
    pub initialized: bool,
    #[prost(string, tag="3")]
    pub version: ::prost::alloc::string::String,
    #[prost(bool, tag="4")]
    pub mnemonic_passphrase_enabled: bool,
    #[prost(uint32, tag="5")]
    pub monotonic_increments_remaining: u32,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct InsertRemoveSdCardRequest {
    #[prost(enumeration="insert_remove_sd_card_request::SdCardAction", tag="1")]
    pub action: i32,
}
/// Nested message and enum types in `InsertRemoveSDCardRequest`.
pub mod insert_remove_sd_card_request {
    #[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
    #[repr(i32)]
    pub enum SdCardAction {
        RemoveCard = 0,
        InsertCard = 1,
    }
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ResetRequest {
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct SetDeviceLanguageRequest {
    #[prost(string, tag="1")]
    pub language: ::prost::alloc::string::String,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct SetDeviceNameRequest {
    #[prost(string, tag="1")]
    pub name: ::prost::alloc::string::String,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct SetPasswordRequest {
    #[prost(bytes, tag="1")]
    pub entropy: ::prost::alloc::vec::Vec<u8>,
}
/// Should be sent every X seconds (TBD) unless the firmware already is busy with a command.
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BitBoxBaseHeartbeatRequest {
    #[prost(enumeration="bit_box_base_heartbeat_request::StateCode", tag="1")]
    pub state_code: i32,
    #[prost(enumeration="bit_box_base_heartbeat_request::DescriptionCode", tag="2")]
    pub description_code: i32,
}
/// Nested message and enum types in `BitBoxBaseHeartbeatRequest`.
pub mod bit_box_base_heartbeat_request {
    #[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
    #[repr(i32)]
    pub enum StateCode {
        Idle = 0,
        Working = 1,
        Warning = 2,
        Error = 3,
    }
    #[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
    #[repr(i32)]
    pub enum DescriptionCode {
        Empty = 0,
        InitialBlockSync = 1,
        DownloadUpdate = 2,
        OutOfDiskSpace = 3,
        RedisError = 4,
        Reboot = 5,
        Shutdown = 6,
        UpdateFailed = 7,
        NoNetworkConnection = 8,
    }
}
/// This will display the first 20 characters of the base32 encoded version of
/// the provided msg
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BitBoxBaseConfirmPairingRequest {
    #[prost(bytes, tag="1")]
    pub msg: ::prost::alloc::vec::Vec<u8>,
}
/// Optional fields can be represented by a "oneof" with only one field in it.
/// All fields are technically optional. But in reality the default value for the type will be set.
/// It is therefore impossible to distinguish between the default value and if the value wasn't set.
/// So any fields that have a default value which also is a valid value can use this method to send
/// an empty value.
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BitBoxBaseSetConfigRequest {
    #[prost(enumeration="bit_box_base_set_config_request::StatusLedMode", tag="1")]
    pub status_led_mode: i32,
    #[prost(enumeration="bit_box_base_set_config_request::StatusScreenMode", tag="2")]
    pub status_screen_mode: i32,
    /// Empty string means unsetting the hostname
    #[prost(string, tag="4")]
    pub hostname: ::prost::alloc::string::String,
    /// 0.0.0.0 which is the default value of ip is also a valid IP, use the oneof-trick to determine
    /// if IP wasn't set in the message.
    #[prost(oneof="bit_box_base_set_config_request::IpOption", tags="3")]
    pub ip_option: ::core::option::Option<bit_box_base_set_config_request::IpOption>,
}
/// Nested message and enum types in `BitBoxBaseSetConfigRequest`.
pub mod bit_box_base_set_config_request {
    #[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
    #[repr(i32)]
    pub enum StatusLedMode {
        /// display on led when status is IDLE, WORKING, WARNING and ERROR
        LedAlways = 0,
        /// display on led when status is WORKING, WARNING and ERROR
        LedOnWorking = 1,
        /// display on led when status is WARNING and ERROR
        LedOnWarning = 2,
        /// display on led when status is ERROR
        LedOnError = 3,
    }
    #[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
    #[repr(i32)]
    pub enum StatusScreenMode {
        /// display on screen when status is IDLE, WORKING, WARNING and ERROR
        ScreenAlways = 0,
        /// display on screen when status is WORKING, WARNING and ERROR
        ScreenOnWorking = 1,
        /// display on screen when status is WARNING and ERROR
        ScreenOnWarning = 2,
        /// display on screen when status is ERROR
        ScreenOnError = 3,
    }
    /// 0.0.0.0 which is the default value of ip is also a valid IP, use the oneof-trick to determine
    /// if IP wasn't set in the message.
    #[derive(Clone, PartialEq, ::prost::Oneof)]
    pub enum IpOption {
        #[prost(bytes, tag="3")]
        Ip(::prost::alloc::vec::Vec<u8>),
    }
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BitBoxBaseDisplayStatusRequest {
    #[prost(uint32, tag="1")]
    pub duration: u32,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BitBoxBaseRequest {
    #[prost(oneof="bit_box_base_request::Request", tags="1, 2, 3, 4")]
    pub request: ::core::option::Option<bit_box_base_request::Request>,
}
/// Nested message and enum types in `BitBoxBaseRequest`.
pub mod bit_box_base_request {
    #[derive(Clone, PartialEq, ::prost::Oneof)]
    pub enum Request {
        #[prost(message, tag="1")]
        Heartbeat(super::BitBoxBaseHeartbeatRequest),
        #[prost(message, tag="2")]
        SetConfig(super::BitBoxBaseSetConfigRequest),
        #[prost(message, tag="3")]
        ConfirmPairing(super::BitBoxBaseConfirmPairingRequest),
        #[prost(message, tag="4")]
        DisplayStatus(super::BitBoxBaseDisplayStatusRequest),
    }
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BtcScriptConfig {
    #[prost(oneof="btc_script_config::Config", tags="1, 2")]
    pub config: ::core::option::Option<btc_script_config::Config>,
}
/// Nested message and enum types in `BTCScriptConfig`.
pub mod btc_script_config {
    #[derive(Clone, PartialEq, ::prost::Message)]
    pub struct Multisig {
        #[prost(uint32, tag="1")]
        pub threshold: u32,
        /// xpubs are acount-level xpubs. Addresses are going to be derived from it using: m/<change>/<receive>.
        /// The number of xpubs defines the number of cosigners.
        #[prost(message, repeated, tag="2")]
        pub xpubs: ::prost::alloc::vec::Vec<super::XPub>,
        /// Index to the xpub of our keystore in xpubs. The keypath to it is provided via
        /// BTCPubRequest/BTCSignInit.
        #[prost(uint32, tag="3")]
        pub our_xpub_index: u32,
    }
    /// SimpleType is a "simple" script: one public key, no additional inputs.
    #[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
    #[repr(i32)]
    pub enum SimpleType {
        P2wpkhP2sh = 0,
        P2wpkh = 1,
    }
    #[derive(Clone, PartialEq, ::prost::Oneof)]
    pub enum Config {
        #[prost(enumeration="SimpleType", tag="1")]
        SimpleType(i32),
        #[prost(message, tag="2")]
        Multisig(Multisig),
    }
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BtcPubRequest {
    #[prost(enumeration="BtcCoin", tag="1")]
    pub coin: i32,
    #[prost(uint32, repeated, tag="2")]
    pub keypath: ::prost::alloc::vec::Vec<u32>,
    #[prost(bool, tag="5")]
    pub display: bool,
    #[prost(oneof="btc_pub_request::Output", tags="3, 4")]
    pub output: ::core::option::Option<btc_pub_request::Output>,
}
/// Nested message and enum types in `BTCPubRequest`.
pub mod btc_pub_request {
    #[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
    #[repr(i32)]
    pub enum XPubType {
        Tpub = 0,
        Xpub = 1,
        Ypub = 2,
        /// zpub
        Zpub = 3,
        /// vpub
        Vpub = 4,
        Upub = 5,
        /// Vpub
        CapitalVpub = 6,
        /// Zpub
        CapitalZpub = 7,
    }
    #[derive(Clone, PartialEq, ::prost::Oneof)]
    pub enum Output {
        #[prost(enumeration="XPubType", tag="3")]
        XpubType(i32),
        #[prost(message, tag="4")]
        ScriptConfig(super::BtcScriptConfig),
    }
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BtcScriptConfigWithKeypath {
    #[prost(message, optional, tag="2")]
    pub script_config: ::core::option::Option<BtcScriptConfig>,
    #[prost(uint32, repeated, tag="3")]
    pub keypath: ::prost::alloc::vec::Vec<u32>,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BtcSignInitRequest {
    #[prost(enumeration="BtcCoin", tag="1")]
    pub coin: i32,
    /// used script configs in inputs and changes
    #[prost(message, repeated, tag="2")]
    pub script_configs: ::prost::alloc::vec::Vec<BtcScriptConfigWithKeypath>,
    /// must be 1 or 2
    #[prost(uint32, tag="4")]
    pub version: u32,
    #[prost(uint32, tag="5")]
    pub num_inputs: u32,
    #[prost(uint32, tag="6")]
    pub num_outputs: u32,
    /// must be <500000000
    #[prost(uint32, tag="7")]
    pub locktime: u32,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BtcSignNextResponse {
    #[prost(enumeration="btc_sign_next_response::Type", tag="1")]
    pub r#type: i32,
    /// index of the current input or output
    #[prost(uint32, tag="2")]
    pub index: u32,
    /// only as a response to BTCSignInputRequest
    #[prost(bool, tag="3")]
    pub has_signature: bool,
    /// 64 bytes (32 bytes big endian R, 32 bytes big endian S). Only if has_signature is true.
    #[prost(bytes, tag="4")]
    pub signature: ::prost::alloc::vec::Vec<u8>,
    /// Previous tx's input/output index in case of PREV_INPUT or PREV_OUTPUT, for the input at `index`.
    #[prost(uint32, tag="5")]
    pub prev_index: u32,
}
/// Nested message and enum types in `BTCSignNextResponse`.
pub mod btc_sign_next_response {
    #[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
    #[repr(i32)]
    pub enum Type {
        Input = 0,
        Output = 1,
        Done = 2,
        /// For the previous transaction at input `index`.
        PrevtxInit = 3,
        PrevtxInput = 4,
        PrevtxOutput = 5,
    }
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BtcSignInputRequest {
    #[prost(bytes, tag="1")]
    pub prev_out_hash: ::prost::alloc::vec::Vec<u8>,
    #[prost(uint32, tag="2")]
    pub prev_out_index: u32,
    #[prost(uint64, tag="3")]
    pub prev_out_value: u64,
    /// must be 0xffffffff-2, 0xffffffff-1 or 0xffffffff
    #[prost(uint32, tag="4")]
    pub sequence: u32,
    /// all inputs must be ours.
    #[prost(uint32, repeated, tag="6")]
    pub keypath: ::prost::alloc::vec::Vec<u32>,
    /// References a script config from BTCSignInitRequest
    #[prost(uint32, tag="7")]
    pub script_config_index: u32,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BtcSignOutputRequest {
    #[prost(bool, tag="1")]
    pub ours: bool,
    /// if ours is false
    #[prost(enumeration="BtcOutputType", tag="2")]
    pub r#type: i32,
    /// 20 bytes for p2pkh, p2sh, pw2wpkh. 32 bytes for p2wsh.
    #[prost(uint64, tag="3")]
    pub value: u64,
    /// if ours is false
    #[prost(bytes, tag="4")]
    pub hash: ::prost::alloc::vec::Vec<u8>,
    /// if ours is true
    #[prost(uint32, repeated, tag="5")]
    pub keypath: ::prost::alloc::vec::Vec<u32>,
    /// If ours is true. References a script config from BTCSignInitRequest
    #[prost(uint32, tag="6")]
    pub script_config_index: u32,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BtcScriptConfigRegistration {
    #[prost(enumeration="BtcCoin", tag="1")]
    pub coin: i32,
    #[prost(message, optional, tag="2")]
    pub script_config: ::core::option::Option<BtcScriptConfig>,
    #[prost(uint32, repeated, tag="3")]
    pub keypath: ::prost::alloc::vec::Vec<u32>,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BtcSuccess {
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BtcIsScriptConfigRegisteredRequest {
    #[prost(message, optional, tag="1")]
    pub registration: ::core::option::Option<BtcScriptConfigRegistration>,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BtcIsScriptConfigRegisteredResponse {
    #[prost(bool, tag="1")]
    pub is_registered: bool,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BtcRegisterScriptConfigRequest {
    #[prost(message, optional, tag="1")]
    pub registration: ::core::option::Option<BtcScriptConfigRegistration>,
    #[prost(string, tag="2")]
    pub name: ::prost::alloc::string::String,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BtcPrevTxInitRequest {
    #[prost(uint32, tag="1")]
    pub version: u32,
    #[prost(uint32, tag="2")]
    pub num_inputs: u32,
    #[prost(uint32, tag="3")]
    pub num_outputs: u32,
    #[prost(uint32, tag="4")]
    pub locktime: u32,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BtcPrevTxInputRequest {
    #[prost(bytes, tag="1")]
    pub prev_out_hash: ::prost::alloc::vec::Vec<u8>,
    #[prost(uint32, tag="2")]
    pub prev_out_index: u32,
    #[prost(bytes, tag="3")]
    pub signature_script: ::prost::alloc::vec::Vec<u8>,
    #[prost(uint32, tag="4")]
    pub sequence: u32,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BtcPrevTxOutputRequest {
    #[prost(uint64, tag="1")]
    pub value: u64,
    #[prost(bytes, tag="2")]
    pub pubkey_script: ::prost::alloc::vec::Vec<u8>,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BtcRequest {
    #[prost(oneof="btc_request::Request", tags="1, 2, 3, 4, 5")]
    pub request: ::core::option::Option<btc_request::Request>,
}
/// Nested message and enum types in `BTCRequest`.
pub mod btc_request {
    #[derive(Clone, PartialEq, ::prost::Oneof)]
    pub enum Request {
        #[prost(message, tag="1")]
        IsScriptConfigRegistered(super::BtcIsScriptConfigRegisteredRequest),
        #[prost(message, tag="2")]
        RegisterScriptConfig(super::BtcRegisterScriptConfigRequest),
        #[prost(message, tag="3")]
        PrevtxInit(super::BtcPrevTxInitRequest),
        #[prost(message, tag="4")]
        PrevtxInput(super::BtcPrevTxInputRequest),
        #[prost(message, tag="5")]
        PrevtxOutput(super::BtcPrevTxOutputRequest),
    }
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct BtcResponse {
    #[prost(oneof="btc_response::Response", tags="1, 2, 3")]
    pub response: ::core::option::Option<btc_response::Response>,
}
/// Nested message and enum types in `BTCResponse`.
pub mod btc_response {
    #[derive(Clone, PartialEq, ::prost::Oneof)]
    pub enum Response {
        #[prost(message, tag="1")]
        Success(super::BtcSuccess),
        #[prost(message, tag="2")]
        IsScriptConfigRegistered(super::BtcIsScriptConfigRegisteredResponse),
        #[prost(message, tag="3")]
        SignNext(super::BtcSignNextResponse),
    }
}
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
#[repr(i32)]
pub enum BtcCoin {
    Btc = 0,
    Tbtc = 1,
    Ltc = 2,
    Tltc = 3,
}
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
#[repr(i32)]
pub enum BtcOutputType {
    Unknown = 0,
    P2pkh = 1,
    P2sh = 2,
    P2wpkh = 3,
    P2wsh = 4,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct EthPubRequest {
    #[prost(uint32, repeated, tag="1")]
    pub keypath: ::prost::alloc::vec::Vec<u32>,
    #[prost(enumeration="EthCoin", tag="2")]
    pub coin: i32,
    #[prost(enumeration="eth_pub_request::OutputType", tag="3")]
    pub output_type: i32,
    #[prost(bool, tag="4")]
    pub display: bool,
    #[prost(bytes, tag="5")]
    pub contract_address: ::prost::alloc::vec::Vec<u8>,
}
/// Nested message and enum types in `ETHPubRequest`.
pub mod eth_pub_request {
    #[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
    #[repr(i32)]
    pub enum OutputType {
        Address = 0,
        Xpub = 1,
    }
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct EthSignRequest {
    #[prost(enumeration="EthCoin", tag="1")]
    pub coin: i32,
    #[prost(uint32, repeated, tag="2")]
    pub keypath: ::prost::alloc::vec::Vec<u32>,
    /// smallest big endian serialization, max. 16 bytes
    #[prost(bytes, tag="3")]
    pub nonce: ::prost::alloc::vec::Vec<u8>,
    /// smallest big endian serialization, max. 16 bytes
    #[prost(bytes, tag="4")]
    pub gas_price: ::prost::alloc::vec::Vec<u8>,
    /// smallest big endian serialization, max. 16 bytes
    #[prost(bytes, tag="5")]
    pub gas_limit: ::prost::alloc::vec::Vec<u8>,
    /// 20 byte recipient
    #[prost(bytes, tag="6")]
    pub recipient: ::prost::alloc::vec::Vec<u8>,
    /// smallest big endian serialization, max. 32 bytes
    #[prost(bytes, tag="7")]
    pub value: ::prost::alloc::vec::Vec<u8>,
    #[prost(bytes, tag="8")]
    pub data: ::prost::alloc::vec::Vec<u8>,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct EthSignMessageRequest {
    #[prost(enumeration="EthCoin", tag="1")]
    pub coin: i32,
    #[prost(uint32, repeated, tag="2")]
    pub keypath: ::prost::alloc::vec::Vec<u32>,
    #[prost(bytes, tag="3")]
    pub msg: ::prost::alloc::vec::Vec<u8>,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct EthSignResponse {
    /// 65 bytes, last byte is the recid
    #[prost(bytes, tag="1")]
    pub signature: ::prost::alloc::vec::Vec<u8>,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct EthRequest {
    #[prost(oneof="eth_request::Request", tags="1, 2, 3")]
    pub request: ::core::option::Option<eth_request::Request>,
}
/// Nested message and enum types in `ETHRequest`.
pub mod eth_request {
    #[derive(Clone, PartialEq, ::prost::Oneof)]
    pub enum Request {
        #[prost(message, tag="1")]
        Pub(super::EthPubRequest),
        #[prost(message, tag="2")]
        Sign(super::EthSignRequest),
        #[prost(message, tag="3")]
        SignMsg(super::EthSignMessageRequest),
    }
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct EthResponse {
    #[prost(oneof="eth_response::Response", tags="1, 2")]
    pub response: ::core::option::Option<eth_response::Response>,
}
/// Nested message and enum types in `ETHResponse`.
pub mod eth_response {
    #[derive(Clone, PartialEq, ::prost::Oneof)]
    pub enum Response {
        #[prost(message, tag="1")]
        Pub(super::PubResponse),
        #[prost(message, tag="2")]
        Sign(super::EthSignResponse),
    }
}
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord, ::prost::Enumeration)]
#[repr(i32)]
pub enum EthCoin {
    Eth = 0,
    RopstenEth = 1,
    RinkebyEth = 2,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ElectrumEncryptionKeyRequest {
    #[prost(uint32, repeated, tag="1")]
    pub keypath: ::prost::alloc::vec::Vec<u32>,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ElectrumEncryptionKeyResponse {
    #[prost(string, tag="1")]
    pub key: ::prost::alloc::string::String,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ShowMnemonicRequest {
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RestoreFromMnemonicRequest {
    #[prost(uint32, tag="1")]
    pub timestamp: u32,
    #[prost(int32, tag="2")]
    pub timezone_offset: i32,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct SetMnemonicPassphraseEnabledRequest {
    #[prost(bool, tag="1")]
    pub enabled: bool,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RandomNumberResponse {
    #[prost(bytes, tag="1")]
    pub number: ::prost::alloc::vec::Vec<u8>,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RandomNumberRequest {
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RebootRequest {
}
/// Deprecated, last used in v1.0.0
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct PerformAttestationRequest {
    /// 32 bytes challenge.
    #[prost(bytes, tag="1")]
    pub challenge: ::prost::alloc::vec::Vec<u8>,
}
/// Deprecated, last used in v1.0.0
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct PerformAttestationResponse {
    #[prost(bytes, tag="1")]
    pub bootloader_hash: ::prost::alloc::vec::Vec<u8>,
    #[prost(bytes, tag="2")]
    pub device_pubkey: ::prost::alloc::vec::Vec<u8>,
    #[prost(bytes, tag="3")]
    pub certificate: ::prost::alloc::vec::Vec<u8>,
    #[prost(bytes, tag="4")]
    pub root_pubkey_identifier: ::prost::alloc::vec::Vec<u8>,
    #[prost(bytes, tag="5")]
    pub challenge_signature: ::prost::alloc::vec::Vec<u8>,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Error {
    #[prost(int32, tag="1")]
    pub code: i32,
    #[prost(string, tag="2")]
    pub message: ::prost::alloc::string::String,
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Success {
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Request {
    #[prost(oneof="request::Request", tags="1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26")]
    pub request: ::core::option::Option<request::Request>,
}
/// Nested message and enum types in `Request`.
pub mod request {
    #[derive(Clone, PartialEq, ::prost::Oneof)]
    pub enum Request {
        #[prost(message, tag="1")]
        RandomNumber(super::RandomNumberRequest),
        #[prost(message, tag="2")]
        DeviceName(super::SetDeviceNameRequest),
        #[prost(message, tag="3")]
        DeviceLanguage(super::SetDeviceLanguageRequest),
        #[prost(message, tag="4")]
        DeviceInfo(super::DeviceInfoRequest),
        #[prost(message, tag="5")]
        SetPassword(super::SetPasswordRequest),
        #[prost(message, tag="6")]
        CreateBackup(super::CreateBackupRequest),
        #[prost(message, tag="7")]
        ShowMnemonic(super::ShowMnemonicRequest),
        #[prost(message, tag="8")]
        BtcPub(super::BtcPubRequest),
        #[prost(message, tag="9")]
        BtcSignInit(super::BtcSignInitRequest),
        #[prost(message, tag="10")]
        BtcSignInput(super::BtcSignInputRequest),
        #[prost(message, tag="11")]
        BtcSignOutput(super::BtcSignOutputRequest),
        #[prost(message, tag="12")]
        InsertRemoveSdcard(super::InsertRemoveSdCardRequest),
        #[prost(message, tag="13")]
        CheckSdcard(super::CheckSdCardRequest),
        #[prost(message, tag="14")]
        SetMnemonicPassphraseEnabled(super::SetMnemonicPassphraseEnabledRequest),
        #[prost(message, tag="15")]
        ListBackups(super::ListBackupsRequest),
        #[prost(message, tag="16")]
        RestoreBackup(super::RestoreBackupRequest),
        #[prost(message, tag="17")]
        PerformAttestation(super::PerformAttestationRequest),
        #[prost(message, tag="18")]
        Reboot(super::RebootRequest),
        #[prost(message, tag="19")]
        CheckBackup(super::CheckBackupRequest),
        #[prost(message, tag="20")]
        Eth(super::EthRequest),
        #[prost(message, tag="21")]
        Reset(super::ResetRequest),
        #[prost(message, tag="22")]
        RestoreFromMnemonic(super::RestoreFromMnemonicRequest),
        #[prost(message, tag="23")]
        Bitboxbase(super::BitBoxBaseRequest),
        #[prost(message, tag="24")]
        Fingerprint(super::RootFingerprintRequest),
        #[prost(message, tag="25")]
        Btc(super::BtcRequest),
        #[prost(message, tag="26")]
        ElectrumEncryptionKey(super::ElectrumEncryptionKeyRequest),
    }
}
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Response {
    #[prost(oneof="response::Response", tags="1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14")]
    pub response: ::core::option::Option<response::Response>,
}
/// Nested message and enum types in `Response`.
pub mod response {
    #[derive(Clone, PartialEq, ::prost::Oneof)]
    pub enum Response {
        #[prost(message, tag="1")]
        Success(super::Success),
        #[prost(message, tag="2")]
        Error(super::Error),
        #[prost(message, tag="3")]
        RandomNumber(super::RandomNumberResponse),
        #[prost(message, tag="4")]
        DeviceInfo(super::DeviceInfoResponse),
        #[prost(message, tag="5")]
        Pub(super::PubResponse),
        #[prost(message, tag="6")]
        BtcSignNext(super::BtcSignNextResponse),
        #[prost(message, tag="7")]
        ListBackups(super::ListBackupsResponse),
        #[prost(message, tag="8")]
        CheckBackup(super::CheckBackupResponse),
        #[prost(message, tag="9")]
        PerformAttestation(super::PerformAttestationResponse),
        #[prost(message, tag="10")]
        CheckSdcard(super::CheckSdCardResponse),
        #[prost(message, tag="11")]
        Eth(super::EthResponse),
        #[prost(message, tag="12")]
        Fingerprint(super::RootFingerprintResponse),
        #[prost(message, tag="13")]
        Btc(super::BtcResponse),
        #[prost(message, tag="14")]
        ElectrumEncryptionKey(super::ElectrumEncryptionKeyResponse),
    }
}
