---
records:
    - id: BQ5ENQR67M
      kind: monograph
      title: 'Solving Problems in Mathematical Analysis, Part I: Sets, Functions, Limits, Derivatives, Integrals, Sequences and Series'
      creators:
        - name: Tomasz Radożycki
          role: author
      date: "2020"
      msc:
        - code: 26-01
          from: zbmath_search
        - code: 00A07
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2020"
          ids:
            doi: 10.1007/978-3-030-35844-0
            zbl: "1452.26002"
            zbl_id: "7156982"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2020"
              ids:
                isbn:
                    - "9783030358433"
                    - "9783030358440"
              access:
                class: record
      relations:
        - kind: part_of
          to: AQAR17SPHM
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-030-35844-0
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "7156982"
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
