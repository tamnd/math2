---
records:
    - id: NNG35N4QAA
      kind: monograph
      title: An Introduction to Enumeration
      creators:
        - name: Alan Camina
          role: author
        - name: Barry Lewis
          role: author
      date: "2011"
      msc:
        - code: 05-01
          from: zbmath_search
        - code: 05A15
          from: zbmath_search
        - code: 97K20
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2011"
          ids:
            doi: 10.1007/978-0-85729-600-9
            zbl: "1230.05001"
            zbl_id: "5911867"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer London
              date: "2011"
              ids:
                isbn:
                    - "9780857295996"
                    - "9780857296009"
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
          native_id: 10.1007/978-0-85729-600-9
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "5911867"
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
