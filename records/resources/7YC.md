---
records:
    - id: 7YC8QY0SEJ
      kind: monograph
      title: Classical Theory of Algebraic Numbers
      creators:
        - name: Paulo Ribenboim
          role: author
      date: "2001"
      msc:
        - code: 11Rxx
          from: zbmath_search
        - code: 11-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2001"
          ids:
            doi: 10.1007/978-0-387-21690-4
            zbl: "1082.11065"
            zbl_id: "1601797"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2001"
              ids:
                isbn:
                    - "9781441928702"
                    - "9780387216904"
              access:
                class: record
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-0-387-21690-4
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "1601797"
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
