---
records:
    - id: K8X4EZEJJ4
      kind: monograph
      title: Measure, Integral and Probability
      creators:
        - name: Marek Capiński
          role: author
        - name: Peter Ekkehard Kopp
          role: author
      date: "1999"
      msc:
        - code: 28-01
          from: zbmath_search
        - code: 60-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1999"
          ids:
            doi:
                - 10.1007/978-1-4471-0645-6
                - 10.1007/978-1-4471-3631-6
            zbl: "1068.28500"
            zbl_id: "1218293"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer London
              date: "2004"
              ids:
                isbn:
                    - "9781852337810"
                    - "9781447106456"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer London
              date: "1999"
              ids:
                isbn:
                    - "9783540762607"
                    - "9781447136316"
              access:
                class: record
      relations:
        - kind: part_of
          to: 3YXAC8SZBF
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4471-0645-6
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4471-3631-6
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "1218293"
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
