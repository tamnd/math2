---
records:
    - id: PEF0D814MP
      kind: monograph
      title: 'Point-Set Topology: A Working Textbook'
      creators:
        - name: Rafael López
          role: author
          ids:
            orcid: 0000-0003-3108-7009
      date: "2024"
      msc:
        - code: 54-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2024"
          ids:
            doi: 10.1007/978-3-031-58513-5
            zbl: "1554.54001"
            zbl_id: "7862873"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2024"
              ids:
                isbn:
                    - "9783031585128"
                    - "9783031585135"
              access:
                class: record
      relations:
        - kind: part_of
          to: 3YXAC8SZBF
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-031-58513-5
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "7862873"
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
