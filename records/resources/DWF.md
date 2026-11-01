---
records:
    - id: DWF2JGHGAE
      kind: monograph
      title: The Radon Transform
      creators:
        - name: Sigurdur Helgason
          role: author
      date: "1980"
      msc:
        - code: 43A85
          from: zbmath_search
        - code: 43-02
          from: zbmath_search
        - code: 44-02
          from: zbmath_search
        - code: 44A15
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1980"
          ids:
            doi:
                - 10.1007/978-1-4757-1463-0
                - 10.1007/978-1-4899-6765-7
            zbl: "0453.43011"
            zbl_id: "3708976"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer US
              date: "1999"
              ids:
                isbn:
                    - "9781475714654"
                    - "9781475714630"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Birkhäuser Boston
              date: "1980"
              ids:
                isbn:
                    - "9781489967671"
                    - "9781489967657"
              access:
                class: record
      relations:
        - kind: part_of
          to: VS2PFDMCR5
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-1463-0
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4899-6765-7
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3708976"
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
