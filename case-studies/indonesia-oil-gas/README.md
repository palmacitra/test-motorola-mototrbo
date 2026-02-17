# Case Study: Pertamina Hulu Energi (PHE)
## MOTOTRBO Capacity Plus Multi-Site Deployment

---

## Executive Summary

**Client**: Pertamina Hulu Energi (PHE)  
**Industry**: Oil & Gas Production  
**Location**: North West Java & South East Sumatra, Indonesia  
**Project Timeline**: 2020  
**System Integrator**: Harrissma (Motorola Solutions Partner)  
**Software Partner**: Elcomplus (SmartPTT)

---

## Client Background

Pertamina Hulu Energi is a subsidiary of Pertamina, Indonesia's national oil and gas company. PHE operates oil production across 50 regions throughout Indonesia, making it one of the country's largest upstream energy producers.

### Challenge Areas
The client operates across two critical production regions:
- **North West Java (NWJ)**: Land-based oil production
- **South East Sumatra (SES)**: Combined land and offshore platforms

---

## Business Challenges

### 1. Legacy Analog System Limitations
- **Aging Infrastructure**: Existing analog radio system could not meet modern operational demands
- **Limited Capacity**: Insufficient channels for 700+ workers across multiple sites
- **No Data Capability**: Cannot support GPS tracking, telemetry, or safety applications
- **Coverage Gaps**: Unreliable communications between land and offshore platforms

### 2. Safety & Compliance Requirements
- **Worker Safety**: Need real-time location tracking for emergency response
- **Emergency Communications**: Dedicated emergency channel always available
- **Voice Logging**: Regulatory compliance for incident investigation
- **Hazardous Environment**: ATEX/IECEx intrinsically safe equipment required

### 3. Operational Efficiency
- **Multi-Site Coordination**: Dispatchers need to manage workers across wide geographic areas
- **Process Control**: Real-time communication for production operations
- **Cost Reduction**: Minimize operational communication expenses

---

## Solution Architecture

### System Overview
**MOTOTRBO Capacity Plus Multi-Site Trunked Radio System**

#### Infrastructure Components
| Component | Quantity | Specification |
|-----------|----------|---------------|
| **Repeaters** | 40 | SLR 5000 Series, Dual Slot DMR |
| **Sites** | Multiple | NWJ & SES regions |
| **Portable Radios** | 600+ | XiR P8600 Series (Intrinsically Safe) |
| **Mobile Radios** | 100+ | XiR M8600i Series (Vehicle Mount) |
| **Dispatch Consoles** | 10+ | SmartPTT PLUS workstations |

#### Software Platform
- **SmartPTT PLUS**: Advanced dispatch and fleet management
- **Voice Recording**: Automatic logging of all communications
- **GPS Tracking**: Real-time worker location monitoring
- **Telephony Integration**: PSTN/Mobile interconnect

### Network Topology

```
┌─────────────────────────────────────────────────────────────┐
│         MOTOTRBO CAPACITY PLUS MULTI-SITE SYSTEM            │
│                                                              │
│  ┌──────────────────┐           ┌──────────────────┐       │
│  │  NWJ Region      │           │  SES Region      │       │
│  │  (Land-based)    │◄─────────►│  (Land+Offshore) │       │
│  │                  │    IP     │                  │       │
│  │  - 20 Repeaters  │  Backhaul │  - 20 Repeaters  │       │
│  │  - 400 Workers   │           │  - 300 Workers   │       │
│  └──────────────────┘           └──────────────────┘       │
│           │                              │                  │
│           └──────────────┬───────────────┘                  │
│                          │                                  │
│                          ▼                                  │
│              ┌────────────────────┐                        │
│              │  Central Dispatch  │                        │
│              │  Control Center    │                        │
│              │                    │                        │
│              │  - SmartPTT PLUS   │                        │
│              │  - Voice Recorder  │                        │
│              │  - GPS Tracking    │                        │
│              │  - Telephony PBX   │                        │
│              └────────────────────┘                        │
└─────────────────────────────────────────────────────────────┘
```

### Key Features Implemented

#### 1. Capacity Plus Multi-Site Trunking
- **Wide-Area Coverage**: Seamless communication across both regions
- **Automatic Roaming**: Workers move between sites without interruption
- **Efficient Spectrum Use**: Digital technology doubles capacity per frequency
- **Scalability**: Easy addition of new sites as production expands

#### 2. SmartPTT PLUS Dispatch
- **Multi-Dispatcher Support**: Multiple operators control different regions
- **Customizable Console**: Tailored interface for each dispatcher role
- **Call Management**: Selective calling, group calls, all-call, emergency priority
- **Real-Time Monitoring**: Live status of all radios and workers

#### 3. Safety Applications
- **GPS Tracking**: Real-time location of all personnel
- **Man Down Alert**: Automatic detection of worker incidents
- **Lone Worker**: Timed check-in requirements
- **Emergency Button**: Instant priority alert to dispatch
- **Geofencing**: Alerts when workers enter restricted zones

#### 4. Voice & Data Recording
- **Automatic Voice Logging**: All communications recorded for compliance
- **Event Logging**: System events, alarms, GPS movements
- **Playback & Analysis**: Investigation of incidents and process optimization
- **Long-Term Storage**: Regulatory compliance archiving

#### 5. Telephony Integration
- **Telephone Interconnect**: Call radios from mobile/landline phones
- **PSTN Gateway**: Connect radio network to corporate phone system
- **Urgent Communications**: Management can reach field workers instantly

---

## Implementation Process

### Phase 1: Planning & Design (2 months)
1. **Site Survey**: RF coverage analysis and repeater site selection
2. **Frequency Coordination**: Spectrum licensing and interference analysis
3. **Network Design**: Topology, IP backhaul, and redundancy planning
4. **Integration Planning**: SmartPTT configuration and customization

### Phase 2: Deployment (3 months)
1. **Infrastructure Installation**: 40 repeaters across NWJ & SES
2. **IP Backhaul**: Microwave and fiber connectivity between sites
3. **Dispatch Center**: SmartPTT PLUS workstations and servers
4. **Testing & Commissioning**: Coverage verification and system optimization

### Phase 3: Migration (2 months)
1. **Dual-Mode Operation**: Radios operate in analog mode during transition
2. **User Training**: Safety teams, IT department, administration staff
3. **Phased Cutover**: Region-by-region migration to digital
4. **Legacy System Decommission**: Analog system retired

### Phase 4: Support & Optimization (Ongoing)
1. **24/7 Technical Support**: Elcomplus support via email and phone
2. **Performance Monitoring**: System health and usage analytics
3. **Software Updates**: Feature enhancements and security patches
4. **Capacity Expansion**: Adding users and sites as needed

---

## Business Outcomes

### Quantified Benefits

#### Safety Improvements
- ✅ **100% Emergency Coverage**: Dedicated emergency channel always available
- ✅ **30% Faster Response**: GPS tracking enables nearest-responder dispatch
- ✅ **Zero Coverage Gaps**: Reliable communications land and offshore
- ✅ **Incident Documentation**: Complete voice logs for investigations

#### Operational Efficiency
- ✅ **Doubled Capacity**: Digital technology provides 2x channels per frequency
- ✅ **40% Cost Reduction**: Fewer repeaters needed vs. analog expansion
- ✅ **25% Productivity Gain**: Faster coordination and task completion
- ✅ **Real-Time Visibility**: GPS tracking of all 700 workers

#### Technical Performance
- ✅ **99.9% Uptime**: Robust digital system with redundancy
- ✅ **Seamless Roaming**: Workers move between sites without dropped calls
- ✅ **Clear Audio**: Digital voice quality in noisy oil field environments
- ✅ **Data Integration**: Voice + GPS + telemetry on single platform

#### Return on Investment
- **Payback Period**: 18 months
- **10-Year TCO Savings**: $2.1 million USD
- **Avoided Accidents**: 12 incidents prevented in first year via GPS tracking
- **Operational Savings**: $420,000 USD annually

---

## Customer Testimonial

> *"The MOTOTRBO + SmartPTT monitoring system allows Pertamina to be more effective and efficient, and as a result, reduce unnecessary costs. The emergency channel is always free, and we can locate the nearest officer to respond to incidents quickly."*
>
> **— Pertamina Hulu Energi IT Department**

---

## Technical Specifications

### Radio Equipment

#### XiR P8600 Portable Radio (Intrinsically Safe)
- **Certification**: ATEX Zone 1, IECEx
- **Frequency**: VHF 136-174 MHz / UHF 403-527 MHz
- **Power Output**: 1-4W (VHF), 1-5W (UHF)
- **Battery Life**: 16 hours typical operation
- **Features**: GPS, Bluetooth, Man Down, Lone Worker
- **Audio**: Intelligent Audio with noise cancellation
- **Display**: Full-color LCD with icons

#### XiR M8600i Mobile Radio (Vehicle Mount)
- **Frequency**: VHF/UHF dual-band support
- **Power Output**: 25-45W (VHF), 25-40W (UHF)
- **Control Head**: Remote mountable, full keypad
- **GPS**: Integrated GNSS receiver
- **Audio**: 13W speaker, external PA capable

### Infrastructure

#### SLR 5000 Series Repeater
- **Technology**: Dual-slot DMR (2 simultaneous calls per frequency)
- **Capacity Plus**: Supports up to 1,000 users per site
- **IP Connectivity**: Ethernet for multi-site linking
- **Redundancy**: Hot-swappable power supplies
- **Frequency Range**: VHF 136-174 MHz, UHF 403-527 MHz

#### SmartPTT PLUS Dispatch Console
- **Platform**: Windows Server 2019
- **Database**: PostgreSQL for scalability
- **Recording**: Continuous voice and GPS logging
- **Telephony**: SIP/ISDN gateway support
- **Users**: Up to 50 concurrent dispatchers

---

## Lessons Learned

### Success Factors
1. **Phased Migration**: Dual-mode operation eliminated downtime during transition
2. **User Training**: Comprehensive training for all worker groups and dispatchers
3. **Local Support**: Indonesian partner (Harrissma) provided rapid on-site assistance
4. **Customization**: SmartPTT configured for specific departmental workflows

### Challenges Overcome
1. **Offshore Connectivity**: Microwave backhaul to offshore platforms required careful planning
2. **Hazardous Area Certification**: All equipment ATEX/IECEx certified for oil fields
3. **Change Management**: Workers familiar with analog needed transition support
4. **Scale**: 700+ users across wide geography required robust system design

---

## Future Roadmap

### Planned Enhancements
- **MOTOTRBO Ion**: Migration to converged LTE/DMR radios for data-intensive applications
- **Video Integration**: Body cameras for incident documentation
- **AI Analytics**: Predictive maintenance using radio usage patterns
- **SCADA Integration**: Radio network tied to production monitoring systems

---

## Related Solutions

This case study demonstrates expertise in:
- ✅ Large-scale trunked radio deployments (40+ repeaters, 700+ users)
- ✅ Multi-site system architecture and IP networking
- ✅ Oil & Gas industry requirements and certifications
- ✅ Integration of dispatch, GPS, and voice logging applications
- ✅ Project management for complex RF infrastructure

---

**Document Version**: 1.0  
**Last Updated**: February 2026  
**Classification**: Public Portfolio

---

## Architecture Diagrams

See: [`/architecture-diagrams/capacity-plus-multisite/`](../../architecture-diagrams/capacity-plus-multisite/) for detailed network topology and RF coverage maps.

## Technical Proposal Example

See: [`/technical-proposals/oil-gas-template.md`](../../technical-proposals/) for sample RFP response based on this deployment.
