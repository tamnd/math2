---
records:
    - id: GXX8KFVADE
      kind: monograph
      title: 'The Art of Proof: Basic Training for Deeper Mathematics'
      creators:
        - name: Matthias Beck
          role: author
        - name: Ross Geoghegan
          role: author
      date: "2010"
      msc:
        - code: 00A35
          from: zbmath_search
        - code: 00A05
          from: zbmath_search
        - code: "97E50"
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2010"
          ids:
            doi: 10.1007/978-1-4419-7023-7
            zbl: "1198.00009"
            zbl_id: "5771352"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2010"
              ids:
                isbn:
                    - "9781441970220"
                    - "9781441970237"
              access:
                class: record
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4419-7023-7
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "5771352"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
