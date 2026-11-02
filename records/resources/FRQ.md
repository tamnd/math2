---
records:
    - id: FRQD43KS6Q
      kind: monograph
      title: An Introduction to Mathematical Cryptography
      creators:
        - name: Hoffstein, Jeffrey
          role: author
        - name: Pipher, Jill
          role: author
        - name: Silverman, Joseph H.
          role: author
      date: "2008"
      msc:
        - code: 94-01
          from: zbmath_search
        - code: 94A60
          from: zbmath_search
        - code: 14G50
          from: zbmath_search
        - code: 11T71
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2008"
          ids:
            doi: 10.1007/978-0-387-77993-5
            zbl: "1160.94001"
            zbl_id: "5268072"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2008"
              ids:
                isbn:
                    - "9780387779935"
                    - "9780387779942"
              access:
                class: record
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 dev scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-0-387-77993-5
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "5268072"
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
