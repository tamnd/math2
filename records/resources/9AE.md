---
records:
    - id: 9AE6MY8W47
      kind: monograph
      title: Explorations in Monte Carlo Methods
      creators:
        - name: Ronald W. Shonkwiler
          role: author
        - name: Franklin Mendivil
          role: author
      date: "2009"
      expressions:
        - key: e1
          kind: edition
          date: "2009"
          ids:
            doi:
                - 10.1007/978-0-387-87837-9
                - 10.1007/978-3-031-55964-8
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2009"
              ids:
                isbn:
                    - "9780387878362"
                    - "9780387878379"
            - key: m2
              kind: print
              publisher: Springer Nature Switzerland
              date: "2024"
              ids:
                isbn:
                    - "9783031559631"
                    - "9783031559648"
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-0-387-87837-9
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-031-55964-8
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: 9AEV5357EK
      kind: problem-set
      title: KöMaL Problems in Mathematics, December 2003
      date: 2003-12
      expressions:
        - key: e1
          kind: edition
          date: 2003-12
          structure: 9AEV5357EK/e1.json
      relations:
        - kind: part_of
          to: 4T7QDPBW1N
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: komal
          snapshot: blake3:3658e660acc064da2c1a894c81d6f74fed1bee98fd8e0b9c468109c4c7e40452
          native_id: 2003-12
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
