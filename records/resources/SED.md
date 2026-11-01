---
records:
    - id: SEDFWK2VJ6
      kind: monograph
      title: p-adic Numbers, p-adic Analysis, and Zeta-Functions
      creators:
        - name: Neal Koblitz
          role: author
      date: "1977"
      msc:
        - code: 11S99
          from: zbmath_search
        - code: 12-02
          from: zbmath_search
        - code: 11S45
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1977"
          ids:
            doi:
                - 10.1007/978-1-4612-1112-9
                - 10.1007/978-1-4684-0047-2
            zbl: "0364.12015"
            zbl_id: "3566956"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1984"
              ids:
                isbn:
                    - "9781461270140"
                    - "9781461211129"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer US
              date: "1977"
              ids:
                isbn:
                    - "9781468400496"
                    - "9781468400472"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-1112-9
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-0047-2
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3566956"
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
