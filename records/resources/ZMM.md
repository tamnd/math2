---
records:
    - id: ZMMN38GBWW
      kind: monograph
      title: Séminaire Bourbaki vol. 1973/74 Exposés 436–452
      date: "1975"
      msc:
        - code: 00Bxx
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: fr
          date: "1975"
          ids:
            doi: 10.1007/bfb0066360
            zbl: "0293.00003"
            zbl_id: "3458509"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1975"
              ids:
                isbn:
                    - "9783540070238"
                    - "9783540373100"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0066360
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "3458509"
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
          at: "2026-11-02"
          by: m2 dev scope/1
          note: from in to in
---
