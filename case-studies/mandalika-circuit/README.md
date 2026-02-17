# Case Study: Mandalika International Circuit
## MOTOTRBO Capacity Max for Racing & Events

---

## Executive Summary

**Client**: Mandalika International Circuit  
**Industry**: Motorsports & Events Management  
**Location**: Lombok, Indonesia  
**Track Type**: FIM-grade International Racing Circuit  
**System**: MOTOTRBO Capacity Max  

---

## Client Background

The Mandalika International Circuit is Indonesia's premier motorsports facility located in Lombok. The circuit hosts:
- **MotoGP** World Championship races
- **Superbike** World Championship (WSBK)
- **National racing** events and championships
- **International** conferences and exhibitions

### Facility Overview
- **Track Length**: 4.3 km
- **Corners**: 17 turns
- **Paddock**: Multiple team garages
- **Grandstands**: Capacity for 50,000+ spectators
- **Support Facilities**: Medical center, race control, VIP areas

---

## Communication Challenges

### 1. Mission-Critical Reliability
- **Race Safety**: Instant communication for marshals, medical teams, fire/rescue
- **Event Coordination**: Multiple departments operating simultaneously
- **Zero Downtime**: Any communication failure risks safety and event success
- **Coverage**: Entire 4.3 km track plus paddock and support areas

### 2. Complex Operations
- **Track Marshals**: 100+ positions around circuit reporting incidents
- **Medical Response**: Quick deployment to accident locations
- **Race Control**: Coordination with FIM officials, teams, broadcast
- **Security**: Access control, crowd management, VIP protection
- **Facilities**: Maintenance, catering, cleaning during events
- **Broadcast**: Coordination with TV production crews

### 3. High-Capacity Events
- **Peak Demand**: Thousands of concurrent radio users during race weekends
- **Multiple Groups**: Different talk groups for each department
- **Scalability**: System must handle varying event sizes
- **Interoperability**: Some users need multi-group monitoring

---

## Solution Architecture

### MOTOTRBO Capacity Max System

**Technology**: DMR Tier III Trunked Radio  
**Topology**: Multi-repeater, single-site trunked system  
**Capacity**: 1,000+ concurrent users

#### Infrastructure
| Component | Quantity | Description |
|-----------|----------|-------------|
| **Capacity Max Repeaters** | 6 | SLR 8000 Series, high-capacity |
| **Portable Radios** | 250+ | DP4000e/XiR P8600 Series |
| **Mobile Radios** | 50+ | DM4000e/XiR M8600 (vehicles) |
| **Antenna System** | Multiple | Distributed antenna system (DAS) |
| **Dispatch Console** | 3 | Race control, security, medical |

### Coverage Design

```
┌─────────────────────────────────────────────────────────┐
│         MANDALIKA CIRCUIT - RF COVERAGE MAP             │
│                                                          │
│  ┌──────────────────────────────────────────────┐      │
│  │                MAIN STRAIGHT                  │      │
│  │  [Antenna 1]         [Antenna 2]              │      │
│  └──────────────────────────────────────────────┘      │
│           │                                              │
│  ┌────────┴──────┐                    ┌────────────┐   │
│  │  SECTOR 1     │                    │  SECTOR 3  │   │
│  │ [Antenna 3]   │    ┌────────┐      │[Antenna 6] │   │
│  │               │    │PADDOCK │      │            │   │
│  │               │    │[Ant 5] │      │            │   │
│  └───────────────┘    └────────┘      └────────────┘   │
│           │                                 │            │
│  ┌────────┴──────────────────────────┬─────┘           │
│  │         SECTOR 2                   │                 │
│  │        [Antenna 4]                 │                 │
│  └────────────────────────────────────┘                 │
│                                                          │
│  COVERAGE: 100% track + paddock + support areas         │
└─────────────────────────────────────────────────────────┘
```

### Talk Groups Configuration

| Group ID | Department | Users | Priority |
|----------|-----------|-------|----------|
| **TG 1** | Race Control | 15 | Critical |
| **TG 2** | Track Marshals | 120 | Critical |
| **TG 3** | Medical & Fire | 25 | Emergency |
| **TG 4** | Security | 40 | High |
| **TG 5** | Event Management | 20 | High |
| **TG 6** | Facilities | 30 | Normal |
| **TG 7** | Broadcast Coordination | 15 | Normal |
| **TG 8** | VIP Services | 10 | Normal |
| **TG 9** | Catering & Hospitality | 25 | Low |
| **TG 10** | All-Call Emergency | All | Emergency |

---

## Key Features Implemented

### 1. Capacity Max Trunking
- **Dynamic Channel Allocation**: Channels assigned on-demand
- **Efficient Spectrum Use**: Maximum users per frequency
- **Guaranteed Quality**: No busy signals during critical moments
- **Scalability**: Easy addition of more users or talk groups

### 2. Priority & Preemption
- **Emergency Override**: Medical/fire calls preempt normal traffic
- **Priority Queuing**: Race control messages get immediate access
- **Critical Communications**: Safety always prioritized

### 3. GPS & Location Services
- **Real-Time Tracking**: All radios show location on dispatch map
- **Incident Response**: Find nearest marshal or medical team instantly
- **Man Down Alert**: Automatic emergency if marshal falls
- **Geofencing**: Alerts when vehicles enter restricted zones

### 4. Dispatch Consoles
- **Race Control Console**: Monitor all groups, selective calling
- **Medical Dispatch**: GPS-based deployment, incident logging
- **Security Control**: Access management, emergency coordination

### 5. Radio Features
- **Emergency Button**: One-touch alert to all supervisors
- **Voice Announcement**: Automated track condition announcements
- **Text Messaging**: Silent coordination when voice is not practical
- **Lone Worker**: Timed check-in for isolated positions

---

## Operational Benefits

### Safety Enhancements
✅ **Instant Communication**: Immediate response to track incidents  
✅ **Medical Coordination**: GPS dispatch reduces response time by 35%  
✅ **No Coverage Gaps**: Reliable communications across entire facility  
✅ **Emergency Priority**: Critical calls never blocked  

### Event Management
✅ **Efficient Coordination**: All departments on integrated platform  
✅ **Flexible Scaling**: System handles 50-user practice days to 250-user race weekends  
✅ **Clear Audio**: Digital quality even in noisy grandstand areas  
✅ **Professional Operation**: Meets FIM and international standards  

### Cost Efficiency
✅ **Single Platform**: One system for all departments (vs. multiple solutions)  
✅ **Spectrum Efficiency**: Fewer frequencies required vs. conventional  
✅ **Reduced Rentals**: Permanent system eliminates expensive event rentals  
✅ **Future-Proof**: Software upgrades extend system life  

---

## Use Case: Race Weekend Operations

### Setup (Thursday - Friday Practice)
- 50-80 users active
- Track marshals, medical, basic security
- System testing and frequency coordination

### Qualifying (Saturday)
- 150-200 users active
- Full marshal deployment
- Enhanced medical and fire presence
- Security for paddock and VIP areas

### Race Day (Sunday)
- 250+ users active
- Maximum staffing for safety
- Broadcast coordination team
- All facilities and catering operational
- VIP services active

### Emergency Response Scenario

**Incident**: Crash at Turn 7

1. **Marshal Alert** (5 seconds)
   - Marshal presses emergency button
   - Automatic GPS location sent to Race Control
   - Priority call interrupts all other traffic

2. **Race Control Response** (10 seconds)
   - Reviews incident on video
   - Deploys medical team via GPS dispatch
   - Alerts safety car and flag marshals

3. **Medical Deployment** (90 seconds)
   - Nearest medical team auto-identified by GPS
   - Direct communication with scene marshal
   - Ambulance pre-positioned

4. **Coordination** (ongoing)
   - Race control coordinates with FIM officials
   - Track clearing operation managed
   - Medical transport if needed

**Total Response Time**: <2 minutes from incident to medical arrival

---

## Technical Specifications

### SLR 8000 Series Repeater (Capacity Max)
- **Technology**: DMR Tier III
- **Channels**: 12 traffic channels per repeater
- **Capacity**: 1,000+ users system-wide
- **Coverage**: Up to 50 km² per site
- **Redundancy**: N+1 repeater configuration

### DP4000e Series Portable Radios
- **Frequency**: UHF 403-470 MHz
- **Power**: 1-4W programmable
- **Battery**: 16+ hours operation
- **Features**: GPS, Emergency button, Man Down
- **Audio**: Intelligent Audio, noise suppression
- **Accessories**: Earpieces, speaker mics, surveillance kits

### Distributed Antenna System (DAS)
- **Antennas**: 6 sectors covering track and facilities
- **Combiner**: Multi-channel combining for efficiency
- **Coax**: Low-loss cable to antenna positions
- **Height**: 20-30m towers for optimal coverage

---

## Customer Testimonial

> *"The MOTOTRBO Capacity Max system ensures reliable, efficient communications during races and events at the track. We can coordinate hundreds of staff members instantly, and the GPS tracking helps us respond to incidents faster than ever before."*
>
> **— Mandalika International Circuit Operations Manager**

---

## Lessons Learned

### Success Factors
1. **Pre-Event Planning**: Detailed talk group assignments prevent confusion
2. **Distributed Coverage**: Multiple antennas eliminate dead zones on track
3. **Capacity Headroom**: System handles peak loads with margin for growth
4. **User Training**: All departments trained on emergency procedures

### Best Practices
- Regular system testing before each event
- Backup equipment pool for quick replacements
- Clear escalation procedures for technical issues
- Integration with circuit safety management system

---

## Future Enhancements

### Planned Upgrades
- **WAVE PTX Integration**: Connect smartphones for non-radio personnel
- **Body Cameras**: Video documentation of incidents for medical/safety review
- **AI Analytics**: Pattern recognition for predictive safety improvements
- **IoT Integration**: Connect track sensors to radio network

---

## Related Industry Applications

This solution is applicable to:
- ✅ **Sports Venues**: Stadiums, arenas, golf courses
- ✅ **Theme Parks**: Large amusement and entertainment facilities  
- ✅ **Conventions**: Exhibition centers and conference facilities
- ✅ **Hospitality**: Large hotels, resorts, casino complexes
- ✅ **Airports**: Terminal operations, ground handling
- ✅ **Universities**: Campus safety and facilities management

---

**Document Version**: 1.0  
**Last Updated**: February 2026  
**Classification**: Public Portfolio
